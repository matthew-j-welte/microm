from command_override_checker import command_override_checker


class CommandCompleter:
    def __init__(self) -> None:
        pass

    @command_override_checker
    def complete_docker_build(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_docker_run(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_docker_test(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_done(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_help(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_hooks_combine(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_hooks_delete(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_hooks_publish(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_hooks_un_publish(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_hooks_view(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_local_build(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_local_run(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_local_test(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_minikube_run(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_minikube_test(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_combine(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_delete(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_edit(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_publish(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_start(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_stop(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_un_publish(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_view(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_recorder_visualize(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_status(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_combine(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_templates_delete(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_templates_publish(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_templates_un_publish(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_templates_use(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_templates_view(
        self, text: str, line: str, start_index: int, end_index: int
    ):
        pass

    @command_override_checker
    def complete_docker_build(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_docker_run(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_docker_test(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_hooks_combine(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_hooks_delete(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_hooks_publish(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_hooks_un_publish(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_hooks_view(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_local_build(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_local_run(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_local_test(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_minikube_run(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_minikube_test(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_combine(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_delete(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_edit(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_publish(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_start(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_stop(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_un_publish(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_view(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_recorder_visualize(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_combine(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_delete(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_publish(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_un_publish(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_use(self, text: str, line: str, start_index: int, end_index: int):
        pass

    @command_override_checker
    def complete_templates_view(self, text: str, line: str, start_index: int, end_index: int):
        pass
