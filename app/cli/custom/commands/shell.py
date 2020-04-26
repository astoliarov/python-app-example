# coding: utf-8

from ..infrastructure.command import Command

from IPython import embed


class ShellCommand(Command):

    def __init__(self, app_instance):
        self.app_instance = app_instance

    def get_name(self):
        return "shell"

    def get_help(self) -> str:
        return "executes shell in context of application instance accessible by app_instance variable"

    def execute(self, opts, args) -> None:
        app_instance = self.app_instance
        embed()

