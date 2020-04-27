# coding: utf-8
import argparse
import typing

from .command import Command


class CLI:
    def __init__(self, cli_name: str) -> None:
        self.parser = argparse.ArgumentParser(description=cli_name)
        self.subparsers = self.parser.add_subparsers(help="commands", dest="command")

        self.handlers = (
            {}
        )  # type: typing.Dict[str, typing.Callable[[typing.Dict[typing.Any, typing.Any], typing.Any], None]]

    def register_commands(self, commands: typing.List[Command]) -> None:
        for command in commands:
            self._register_command(command)

    def _register_command(self, command: Command):
        name = command.get_name()

        command_parser = self.subparsers.add_parser(name, help=command.get_help())
        command.add_arguments(parser=command_parser)

        self.handlers[name] = command.execute

    def run(self, opts):
        args = self.parser.parse_args()

        handler = self.handlers[args.command]

        print(args)
        print(opts)

        handler(opts, args)
