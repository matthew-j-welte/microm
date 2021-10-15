# Phase 1

End Goal:

- Have a .microm folder in a repository
- Be able to pass in profiles defined in the .microm file (probably use YAML) to keep things dynamic between repositories
- Once microm is running be able to do the following:
  - Build locally
  - Docker build
  - Local deploy
  - K8s deploy (minkube)

**Stories**

Write functionality for parsing and validating the .microm config(s) being passed in
Refactor sentrain shell code to be more general purpose
