End Goals:

- Be able to pip install microm, have it auto detect all of sentrain's apps and be able to run them both locally and on docker and minikube.
- Be able to create and use hooks
- Be able to create and use recordings
- Be able to create and use run-types
  <!-- - Be able to create and use status-templates -->
  <!-- - Be able to run my-status -->
- Be able to use a multi-file code template to write code

Tasks:

- Map out 'command tree'
- Create skeleton of the application
- Make microm packageable
- Make microm runners packageable
- Architect how you will split commands (by functionality? maybe each top level command gets a class?)
- Architect where you will put the code for:
  - hooks
  - recordings
  - run-types
  - code-template
- Write the core code + unit tests for:
  - hooks
  - recordings
  - run-types
  - code-template
- Write the validator code + unit tests
- Write the microm-init code + unit tests
- Write the config-writer code + unit tests
- Write the config-parser code + unit tests
- Write the local-context and models code + unit tests for local-context
- Write the console-writer code + unit tests MAYBE
