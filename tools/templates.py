def generic_complete_cmd_func(func):
    return f"""
    def complete_{func}(self, *args):
        return self.cmd_completer.complete_{func}(*args)
"""


def generic_do_cmd_func(func):
    return f"""
    def do_{func}(self, *args):
        self.cmd_runner.do_{func}(*args)
"""


def generic_command_completer_func(func):
    return f"""
    def complete_{func}(self, text, line, *args):
        pass
"""


def generic_command_runner_func(func):
    return f"""
    def do_{func}(self, line):
        pass
"""


def get_shell_commands_file(command_functions):
    return (
        f"""import cmd
from command_completer import CommandCompleter
from command_runner import CommandRunner


class MicromShell(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.cmd_completer = CommandCompleter()
        self.cmd_runner = CommandRunner()
"""
        + command_functions
    )


def complete_function_def(func_name):
    return f"def complete_{func_name}(self,"


def do_function_def(func_name):
    return f"def do_{func_name}(self,"
