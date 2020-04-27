# coding: utf-8
from cli.custom.infrastructure.cli_root import CLI
from cli.custom.commands.shell import ShellCommand


def init_cli(name: str, app_instance):
    cli_instance = CLI(name)
    cli_instance.register_commands([ShellCommand(app_instance)])
    return cli_instance
