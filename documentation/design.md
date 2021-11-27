## Thoughts

Im wondering if everything should be centered around the 'modes'

That way once you're fully setup for local for example you can just use that without fail or confusion, instead of having to install a crap ton of cloud CLI's or whatever just to get running locally

Questions:

- What is annoying about local development?
- What is annoying about the link between local and CI/CD code?
-

## Extensibility + Customizability

The key features of microm is (and should always stay) extensibility and customizability

We cant expect to predict every single use case a developer could have when it comes to managing microservices, so they key focus needs to be on allowing users to add their own code if needed.

Maybe we can have templates of the different extensibility options using basic languages like python/javascript/go - otherwise things might get a bit cumbersome

## Features

_Local Build + Run_

_Containerized Build + Run_

_Project Software Install_

- Possibly have an auto install feature (based on params passed to config):
  - If that doesn't work for some reason we could have an extension option
  - Then I guess whatever manual steps there are should require a list of steps
  - If an auto install option doesn't work continually you should suggest a switch to an extension
  - **global**: Shuold probably have a .microm/.statistics file for monitoring things like install failures

_Record lists of commands and rerun them again in one command_

_Code Templates_

- Utilize user created templates that facilitate faster coding
- IN ANY LANGUAGE

_Bootstrap Extensions_

- A term for the steps needed to get up and running with a particular 'mode'
- Be able to authenticate to whichever provider a user is using to deploy
  - Good place for extensions, maybe we give a template and say "write the commands needed to auth to this service"
  - We can have already written extensions for popular providers (minikube is probably a good starting point)
  - So whenever we switch modes, we should do a check for an auth extension (built-in or custom)

_Parsing Extensions_

- Used to give users the ability to parse the output from particular commands and either:

  - Use it to change microm shared state
  - Output some parseable result (possibly a json string used by some CI task)

- _LTG_: Be able to utilize the same exact tasks/steps for CI/CD as for local using an installable custom microm package that has been previously packaged up.
  Examples:

  - ```sh
    sudo apt install microm "<some-unique-url>";
    microm --ci deploy-test
    ```

  ```
  - Or just package it into a docker container and use it that way

  ```

- Do all of this through a config driven approach with very little + very basic rules
