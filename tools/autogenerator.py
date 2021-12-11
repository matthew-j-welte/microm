import os
import sys
from typing import List
import yaml
import templates as autogen_templates


class Autogenerator:
    def __init__(self) -> None:
        self.func_lookup = {
            "all": self.run_all_funcs,
            "shell-commands": self.autogen_microm_shell_cmds,
        }

    def run(self, func: str):
        self.func_lookup[func]()

    def run_all_funcs(self):
        [func() for k, func in self.func_lookup.items() if k is not "all"]

    def autogen_microm_shell_cmds(self):
        commands = yaml.load(open("../data/command-tree.yaml"), Loader=yaml.FullLoader)
        cmd_list = sorted(self._flatten_commands("", commands))
        command_functions_text = "".join(
            [autogen_templates.generic_complete_cmd_func(cmd) for cmd in cmd_list]
            + [autogen_templates.generic_do_cmd_func(cmd) for cmd in cmd_list]
        )
        shell_file_contents = autogen_templates.get_shell_commands_file(
            command_functions_text
        )

        with open("../microm/command_tree/command_shell.py", "w") as shell_file:
            shell_file.write(shell_file_contents)

        with open("../microm/command_tree/command_completer.py", "r") as completer_file:
            completer_file_content = completer_file.read()

        with open("../microm/command_tree/command_completer.py", "w") as completer_file:
            missing_funcs_code = "".join(
                [
                    autogen_templates.generic_command_completer_func(cmd)
                    for cmd in cmd_list
                    if autogen_templates.complete_function_def(cmd)
                    not in completer_file_content
                ]
            )
            completer_file.write(completer_file_content + missing_funcs_code)

        with open("../microm/command_tree/command_runner.py", "r") as runner_file:
            runner_file_content = runner_file.read()

        with open("../microm/command_tree/command_runner.py", "w") as runner_file:
            missing_funcs_code = "".join(
                [
                    autogen_templates.generic_command_runner_func(cmd)
                    for cmd in cmd_list
                    if autogen_templates.do_function_def(cmd) not in runner_file_content
                ]
            )
            runner_file.write(runner_file_content + missing_funcs_code)

        # inject the text into that file

        # open the completer file
        # loop through each line of the file one by one
        # use regex to match against all 'def complete_<cmd>(self,' to determine when a function begins (and the previous has ended)

        # for each command in the command list check if an instance of 'def complete_<cmd>(self,' exists.
        #   If it does - continue
        #   If it doesnt

        # scan the command_completer/command_runner files for any missing complete's/do's
        # for each missing complete and do add a function to the respective file
        # for any commands that exist in the files but not in the command list, throw a heavy warning to remove them or put a @preview tag on them
        # for any newly added complete / do functions, tell the user they need to fill in the functionality

    @classmethod
    def _flatten_commands(cls, cmd: str, subcommands: List[dict]) -> List[str]:
        if subcommands is None or len(subcommands) == 0:
            return [cmd]

        all_cmds = []
        for subcmd in subcommands:
            all_cmds += cls._flatten_commands(
                [*subcmd.keys()][0], [*subcmd.values()][0]
            )

        return [f"{cmd if cmd is '' else (cmd + '_')}{subcmd}" for subcmd in all_cmds]


if __name__ == "__main__":
    func = sys.argv[1]
    Autogenerator().run(func)
