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
        [func() for k, func in self.func_lookup.items() if k != "all"]

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
            completer_file_lines = completer_file.readlines()

        function_name_content_lookup = dict()
        active_function_lines = []
        function_name = None
        command_completer_file = ""
        for line in completer_file_lines:
            stripped_line = line.strip()
            print(stripped_line)
            if stripped_line.startswith("def complete_"):
                if function_name is None:
                    command_completer_file = "".join(active_function_lines)
                else:
                    function_name_content_lookup[function_name] = "".join(
                        [x for x in active_function_lines]
                    )
                function_name = stripped_line.split("def complete_")[1].split("(")[0]
                print(function_name)
                active_function_lines = []
            active_function_lines.append(line)

        # sorted_functions = sorted(function_name_content_lookup.items())
        print(function_name_content_lookup)

        for cmd in cmd_list:
            if cmd not in function_name_content_lookup:
                function_name_content_lookup[
                    cmd
                ] = autogen_templates.generic_command_completer_func(cmd)

        print([x for x, y in sorted(function_name_content_lookup.items())])

        # with open("../microm/command_tree/command_completer.py", "w") as completer_file:
        #     completer_file.write(completer_file_content + missing_funcs_code)

        obsolete_functions = [
            func_name
            for func_name in function_name_content_lookup.keys()
            if func_name not in cmd_list
        ]

        # with open("../microm/command_tree/command_runner.py", "r") as runner_file:
        #     runner_file_content = runner_file.read()

        # missing_funcs_code = "".join(
        #     [
        #         autogen_templates.generic_command_runner_func(cmd)
        #         for cmd in cmd_list
        #         if autogen_templates.do_function_def(cmd) not in runner_file_content
        #     ]
        # )

        # with open("../microm/command_tree/command_runner.py", "w") as runner_file:
        #     runner_file.write(runner_file_content + missing_funcs_code)

        # inject the text into that file

        # open the completer file
        # loop through each line of the file one by one
        # set dictionary to generic value if it doesn't exist otherwise set it to the code block
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

        return [f"{cmd if cmd == '' else (cmd + '_')}{subcmd}" for subcmd in all_cmds]


if __name__ == "__main__":
    func = sys.argv[1]
    Autogenerator().run(func)
