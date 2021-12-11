from command_override_checker import command_override_checker


class CommandRunner:
    def __init__(self) -> None:
        pass

    @command_override_checker
    def do_docker_build(self, line: str):
        pass

    @command_override_checker
    def do_docker_run(self, line: str):
        pass

    @command_override_checker
    def do_docker_test(self, line: str):
        pass

    @command_override_checker
    def do_done(self, line: str):
        pass

    @command_override_checker
    def do_help(self, line: str):
        pass

    @command_override_checker
    def do_hooks_combine(self, line: str):
        pass

    @command_override_checker
    def do_hooks_delete(self, line: str):
        pass

    @command_override_checker
    def do_hooks_publish(self, line: str):
        pass

    @command_override_checker
    def do_hooks_un_publish(self, line: str):
        pass

    @command_override_checker
    def do_hooks_view(self, line: str):
        pass

    @command_override_checker
    def do_local_build(self, line: str):
        pass

    @command_override_checker
    def do_local_run(self, line: str):
        pass

    @command_override_checker
    def do_local_test(self, line: str):
        pass

    @command_override_checker
    def do_minikube_run(self, line: str):
        pass

    @command_override_checker
    def do_minikube_test(self, line: str):
        pass

    @command_override_checker
    def do_recorder_combine(self, line: str):
        pass

    @command_override_checker
    def do_recorder_delete(self, line: str):
        pass

    @command_override_checker
    def do_recorder_edit(self, line: str):
        pass

    @command_override_checker
    def do_recorder_publish(self, line: str):
        pass

    @command_override_checker
    def do_recorder_start(self, line: str):
        pass

    @command_override_checker
    def do_recorder_stop(self, line: str):
        pass

    @command_override_checker
    def do_recorder_un_publish(self, line: str):
        pass

    @command_override_checker
    def do_recorder_view(self, line: str):
        pass

    @command_override_checker
    def do_recorder_visualize(self, line: str):
        pass

    @command_override_checker
    def do_status(self, line: str):
        pass

    @command_override_checker
    def do_templates_combine(self, line: str):
        pass

    @command_override_checker
    def do_templates_delete(self, line: str):
        pass

    @command_override_checker
    def do_templates_publish(self, line: str):
        pass

    @command_override_checker
    def do_templates_un_publish(self, line: str):
        pass

    @command_override_checker
    def do_templates_use(self, line: str):
        pass

    @command_override_checker
    def do_templates_view(self, line: str):
        pass
