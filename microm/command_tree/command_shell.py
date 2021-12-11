import cmd
from command_completer import CommandCompleter
from command_runner import CommandRunner


class MicromShell(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.cmd_completer = CommandCompleter()
        self.cmd_runner = CommandRunner()

    def complete_docker_build(self, *args):
        return self.cmd_completer.complete_docker_build(*args)

    def complete_docker_run(self, *args):
        return self.cmd_completer.complete_docker_run(*args)

    def complete_docker_test(self, *args):
        return self.cmd_completer.complete_docker_test(*args)

    def complete_done(self, *args):
        return self.cmd_completer.complete_done(*args)

    def complete_help(self, *args):
        return self.cmd_completer.complete_help(*args)

    def complete_hooks_combine(self, *args):
        return self.cmd_completer.complete_hooks_combine(*args)

    def complete_hooks_delete(self, *args):
        return self.cmd_completer.complete_hooks_delete(*args)

    def complete_hooks_publish(self, *args):
        return self.cmd_completer.complete_hooks_publish(*args)

    def complete_hooks_un_publish(self, *args):
        return self.cmd_completer.complete_hooks_un_publish(*args)

    def complete_hooks_view(self, *args):
        return self.cmd_completer.complete_hooks_view(*args)

    def complete_local_build(self, *args):
        return self.cmd_completer.complete_local_build(*args)

    def complete_local_run(self, *args):
        return self.cmd_completer.complete_local_run(*args)

    def complete_local_test(self, *args):
        return self.cmd_completer.complete_local_test(*args)

    def complete_minikube_run(self, *args):
        return self.cmd_completer.complete_minikube_run(*args)

    def complete_minikube_test(self, *args):
        return self.cmd_completer.complete_minikube_test(*args)

    def complete_recorder_combine(self, *args):
        return self.cmd_completer.complete_recorder_combine(*args)

    def complete_recorder_delete(self, *args):
        return self.cmd_completer.complete_recorder_delete(*args)

    def complete_recorder_edit(self, *args):
        return self.cmd_completer.complete_recorder_edit(*args)

    def complete_recorder_publish(self, *args):
        return self.cmd_completer.complete_recorder_publish(*args)

    def complete_recorder_start(self, *args):
        return self.cmd_completer.complete_recorder_start(*args)

    def complete_recorder_stop(self, *args):
        return self.cmd_completer.complete_recorder_stop(*args)

    def complete_recorder_un_publish(self, *args):
        return self.cmd_completer.complete_recorder_un_publish(*args)

    def complete_recorder_view(self, *args):
        return self.cmd_completer.complete_recorder_view(*args)

    def complete_recorder_visualize(self, *args):
        return self.cmd_completer.complete_recorder_visualize(*args)

    def complete_status(self, *args):
        return self.cmd_completer.complete_status(*args)

    def complete_templates_combine(self, *args):
        return self.cmd_completer.complete_templates_combine(*args)

    def complete_templates_delete(self, *args):
        return self.cmd_completer.complete_templates_delete(*args)

    def complete_templates_publish(self, *args):
        return self.cmd_completer.complete_templates_publish(*args)

    def complete_templates_un_publish(self, *args):
        return self.cmd_completer.complete_templates_un_publish(*args)

    def complete_templates_use(self, *args):
        return self.cmd_completer.complete_templates_use(*args)

    def complete_templates_view(self, *args):
        return self.cmd_completer.complete_templates_view(*args)

    def do_docker_build(self, *args):
        self.cmd_runner.do_docker_build(*args)

    def do_docker_run(self, *args):
        self.cmd_runner.do_docker_run(*args)

    def do_docker_test(self, *args):
        self.cmd_runner.do_docker_test(*args)

    def do_done(self, *args):
        self.cmd_runner.do_done(*args)

    def do_help(self, *args):
        self.cmd_runner.do_help(*args)

    def do_hooks_combine(self, *args):
        self.cmd_runner.do_hooks_combine(*args)

    def do_hooks_delete(self, *args):
        self.cmd_runner.do_hooks_delete(*args)

    def do_hooks_publish(self, *args):
        self.cmd_runner.do_hooks_publish(*args)

    def do_hooks_un_publish(self, *args):
        self.cmd_runner.do_hooks_un_publish(*args)

    def do_hooks_view(self, *args):
        self.cmd_runner.do_hooks_view(*args)

    def do_local_build(self, *args):
        self.cmd_runner.do_local_build(*args)

    def do_local_run(self, *args):
        self.cmd_runner.do_local_run(*args)

    def do_local_test(self, *args):
        self.cmd_runner.do_local_test(*args)

    def do_minikube_run(self, *args):
        self.cmd_runner.do_minikube_run(*args)

    def do_minikube_test(self, *args):
        self.cmd_runner.do_minikube_test(*args)

    def do_recorder_combine(self, *args):
        self.cmd_runner.do_recorder_combine(*args)

    def do_recorder_delete(self, *args):
        self.cmd_runner.do_recorder_delete(*args)

    def do_recorder_edit(self, *args):
        self.cmd_runner.do_recorder_edit(*args)

    def do_recorder_publish(self, *args):
        self.cmd_runner.do_recorder_publish(*args)

    def do_recorder_start(self, *args):
        self.cmd_runner.do_recorder_start(*args)

    def do_recorder_stop(self, *args):
        self.cmd_runner.do_recorder_stop(*args)

    def do_recorder_un_publish(self, *args):
        self.cmd_runner.do_recorder_un_publish(*args)

    def do_recorder_view(self, *args):
        self.cmd_runner.do_recorder_view(*args)

    def do_recorder_visualize(self, *args):
        self.cmd_runner.do_recorder_visualize(*args)

    def do_status(self, *args):
        self.cmd_runner.do_status(*args)

    def do_templates_combine(self, *args):
        self.cmd_runner.do_templates_combine(*args)

    def do_templates_delete(self, *args):
        self.cmd_runner.do_templates_delete(*args)

    def do_templates_publish(self, *args):
        self.cmd_runner.do_templates_publish(*args)

    def do_templates_un_publish(self, *args):
        self.cmd_runner.do_templates_un_publish(*args)

    def do_templates_use(self, *args):
        self.cmd_runner.do_templates_use(*args)

    def do_templates_view(self, *args):
        self.cmd_runner.do_templates_view(*args)
