## Thoughts

The key features of microm is (and should always stay) extensibility and customizability

We cant expect to predict every single use case a developer could have when it comes to managing microservices, so they key focus needs to be on allowing users to add their own code if needed.

Maybe we can have templates of the different extensibility options using basic languages like python/javascript/go - otherwise things might get a bit cumbersome

Im wondering if everything should be centered around the 'modes'

That way once you're fully setup for local for example you can just use that without fail or confusion, instead of having to install a crap ton of cloud CLI's or whatever just to get running locally

Questions:

- What is annoying about local development?
- What is annoying about the link between local and CI/CD code?
- ***

second guessing making the "mode" the focal point.. because what if you want to run your newly modified app locally, on docker and on minikube.. you'd have to switch to all different modes and then if you have cleanup hooks you're screwed.. so maybe everything should just be based at the 'run' level. Meaning...

we could have hooks for particular runs, built in ones for apps of a certain type (only locally I guess)

## Features

### my-status

- shows a user their project + user level status. meaning, if they're validated to use dotnet, go, python locally, can use docker, minikube etc.
- this is a good alternate to the mode hooks originally planned.

### Local Build + Run

### Containerized Build + Run

### Project Software Install

- Possibly have an auto install feature (based on params passed to config):
  - If that doesn't work for some reason we could have an extension option
  - Then I guess whatever manual steps there are should require a list of steps
  - If an auto install option doesn't work continually you should suggest a switch to an extension
  - **global**: Shuold probably have a .microm/.statistics file for monitoring things like install failures

### Record lists of commands and rerun them again in one command

Example:

```
> start-global-record # or start-user-record
> mode local
> local build all
> unit-test all
> int-test all
> stop record LocalE2E

Saved LocalE2E to global recordings!

> run LocalE2E # Have this autocomplete to the ilst of recordings
```

### Code Templates

Layout:
<template-name>/

- info.yaml
- template.<file-extension>

info.yaml:

```yaml
inputs:
  - MODEL_INPUT_PATH
outputs:
  - ENTITY_NAME
steps:
  - path: "src/Domain/Interfaces/I{{ vars.ENTITY_NAME }}Repository.cs"
    template: { { templates.dotnet-repository } }
  - path: "src/Domain/Repositories/{{ vars.ENTITY_NAME }}Repository.cs"
    template: { { templates.dotnet-repository-interface } }
  - path: "src/Tests/Unit/App.Domain.Unit.Tests/{{ vars.ENTITY_NAME }}RepositoryTests.cs"
    template: { { templates.dotnet-repository-unit-test } }
```

- Utilize user created templates that facilitate faster coding In any language
- Should be able to do dynamic content inside of a file but also for the file paths, for example:

### Bootstrap Extensions

- A term for the steps needed to get up and running with a particular 'mode'
- Be able to authenticate to whichever provider a user is using to deploy
  - Good place for extensions, maybe we give a template and say "write the commands needed to auth to this service"
  - We can have already written extensions for popular providers (minikube is probably a good starting point)
  - So whenever we switch modes, we should do a check for an auth extension (built-in or custom)

### Teardown Extensions

- Runs after a mode is switched off of (or the app terminates)
- Would be a good place to clean up any local resources if desired

### Continually check for missing configuration either by a user or project

- Can intermittently say things like "NOTE: There are 7 missing config values for _testdb_ `run-type` - Adding these can help save time"

### Can have run-types with hooks

- This way if we meed some dynamic vars or need to combine a number of inputs, we can do this here

### Parsing Extensions

- Used to give users the ability to parse the output from particular commands and either:

  - Use it to change microm shared state
  - Output some parseable result (possibly a json string used by some CI task)

### Shutdown Hooks

- Should be able to apply "shutdown hooks" when using microm which specifies actions to take on terminate

### Config/Admin mode

- Go into this mode for modifying any .microm auto gen configs. (update software list best on local versions etc.)

### Template driven "status layouts" to show your apps in different ways

Example:

By Type

```
dotnet |  a2-dotnet-job   a3-dotnet-cronjob   x1-dotnet-app   z1-dotnet-app
       |  RUNNING         RUNNING             RUNNING         RUNNING

Python |  a2-python-job   a3-python-cronjob   x1-python-app   z1-python-app
       |  RUNNING         RUNNING             RUNNING         RUNNING
```

Sample yaml - layouts/language-type-grouping.yaml:

```yaml
dotnet:
  groupby: language
```

By 'Function' (responsibility in the architecture)

```
preprocessors |  a2-dotnet-preprocessor    a3-dotnet-preprocessor    x1-javascript-preprocessor    z1-go-preprocessor
              |  RUNNING                   RUNNING                   RUNNING                       RUNNING

APIs | a2-dotnet-api    a3-dotnet-api    x1-node-api    z1-go-api
       RUNNING          RUNNING          RUNNING        RUNNING
```

Sample yaml - layouts/organized-architecture-layout.yaml:

```yaml
preprocessors:
  apps:
    - a2-dotnet-preprocessor
    - a3-dotnet-preprocessor
    - x1-javascript-preprocessor
    - z1-go-preprocessor
APIs:
  apps:
    - a2-dotnet-api
    - a3-dotnet-api
    - x1-node-api
    - z1-go-api
```

---

## Flow

_For each one of the init steps we could probably have a is-<some-state> function to validate before starting microm_

- install microm
- microm init (inside project directory)
  - are you sure this is your base directory? (<dir>)
  - ask if they'd like us to add the env var for the base directory to their .bashrc / if not do it themselves
  - name of your project (Suggest git/base folder name)
  - if not git: highly recommend enabling it as it will add additional features
  - auto parse apps:
    - find all apps under src/app etc folder and map them to cli tools (dotnet/go)
    - continue? or add/remove apps?
  - based on the technologies specified in the apps gen section, auto create a software list
  - auto create groups file (group for all apps of the same type and do an "all" which only has an empty exlusion list)
  - what do you plan on deploying your apps to? (local,docker,docker-compose,minikube,aks,eks)
  - based on the above auto create the values file for each app
  - point them to the read me
  - init complete
- a user decides he wants to start microm and run his dotnet app(s) locally:

  - `microm`
  - Please select mode: (local, admin, docker, minikube)
  - (sample-project) >> `local`
  - ````
        Mode Set to: __local__

        Bootstrap Hooks: local-bootstrap (microm built-in), clean-local-env
        Teardown Hooks: local-data-snapshots, slocal-teardown (microm built-in)

        Running local-bootstrap (microm built-in) ... PASSED
        Running clean-local-env ... PASSED

        (sample-project) (local) >> build <tab>
        all  compiled-apps  other-apps
        dotnet-sample-app  go-sample-app  old-sample-app  python-sample-app
        (sample-project) (local) >> build dotnet-sample-app

        Building dotnet-sample-app ..... PASSED    (do a sleep every X milliseconds and print a dot until you reach a max of like 6)

        (sample-project) (local) >> run dotnet-sample-app

        Building dotnet-sample-app .. PASSED
        Starting dotnet-sample-app .... STARTED

        Status:
        dotnet-sample-app   (ohther-app)    (some-other-app)
        RUNNING             RUNNING         RUNNING

        (sample-project) (local) >> done

        Running local-data-snapshots ... PASSED
        Running local-teardown (microm built-in) ... PASSED

        Thank you for using microm
    .
        ```
    ````

  ```

  ```

## Architecture

**Top Level**

```
microm/
  .gitignore
  README.md
  setup.py
  microm-cli/
    __init__.py
    run.py
      run():
        if not validator.is_project_initialized():
          bootstrapper.initialize_project()
        if validator.is_project_fully_validated():
          runner.start_microm()
        else:
          # pce!

    validator.py:
      is_project_initialized():
        # check if the .microm folder exists
        # if it does check to ensure at least one app exists under microservices
        # keep trying to init if a user decides they dont want to add apps yet
    cli-runner.py:
      start_microm():
    microm-init.py:
      initialize_project():
        if not validator.is_git_base_directory():
          # warn them to seriously reconsider where they init microm
          # warn them if no git
        # would you like me to add env var to bashrc? microm_myproject=/home/mwelte/github/microm
        configwriter.autogen_service_configs()
        configwriter.autogen_software_config()
        configwriter.autogen_groups_config()
        # what do you plan to deploy your apps to?
        for mode_selected in []:
          configwriter.create_starter_values(mode: mode_selected)
        # point to readme
        # say init complete

    config-writer.py:
      autogen_service_configs():
        # bunch of fancy stuff with looping through src/ app/ etc. and looking for apps
      autogen_software_config():
        # based on app types in services/ folder, and the versions the user has for those cli's, gen a software list yaml
      autogen_groups_config():
        # auto create groups file (group for all apps of the same type and do an "all" which only has an empty exlusion list)
    config-parser.py:
    local-context.py
    models.py (use named tuples or something else here: https://dev.to/izabelakowal/some-ideas-on-how-to-implement-dtos-in-python-be3)
    console-writer.py (handles all output statements, can have built in utilities to make repetitive print tasks easier)
```

**Runners**

```
microm/
  ...
  runners/
    dotnet-runner/
      __init__.py
      setup.py
      ...
    go-runner/
      __init__.py
      setup.py
      ...
```

Each runner should be contained to a seperate module that way a user can upgrade microm whenever they want and not break all their runners

**Need to figure out how to design the link between 'run modes' and different languages**

- could we do just one runner for docker, helm-minikube, docker-compose
  - how could they differ.. lets think
  -
- and then one for each local language?

what are we trying to accomplish.....

we want developers on a team to be able to run,test,automate tasks etc as easily and quickly as possible with some upfront effort on their part, however this effort will be clearly organized, modularized and most importantly extensible.

so our job is to set up a clear and understandable framework for how users can create that automation.

but we also dont just want to make them do all the work.. remember we also want to keep this config based as much as possible

**run types**

in the values.yaml file have:

```yaml
run-types:
  localdb:
    inputs:
      ENV: development
      DATABASE: some-app-dev
  testdb:
    inputs:
      ENV: development
      DATABASE: some-app-test
```

then maybe some overrides in `values.docker.yaml`:

```yaml
run-types:
  localdb:
    inputs:
      ENV: docker-dev
  testdb:
    inputs:
      ENV: docker-dev
```
