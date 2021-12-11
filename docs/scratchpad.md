**YAML Parser**

If you end up using kubectl helm executables from microm code, you should include the latest tested version on release and then
show a warning if the user has a version higher than that.

But best case theres a go pkg that I can use instead of helm or kubectl

**YAML Layout**

```
.microm/
  globals.yaml
  groups.yaml
  microservices/
    game-tracker/
      _helpers.tpl
      values.yaml
      values.local.yaml
      values.docker.yaml
      values.minikube.yaml
    player-tracker/
      _helpers.tpl
      values.yaml
      values.local.yaml
      values.docker.yaml
      values.minikube.yaml
```

Code Design:

Thinking the best solution is to have a struct for each runner type and then simply have generic runner classes, one for each of: local,docker,minikube,etc..

So something like

DotnetProcess:

- localBuild
- localRun

LocalRunner:
process: DotnetProcess

DockerRunner:
process: DotnetProcess

HelmRunner:
process: DotnetProcess
