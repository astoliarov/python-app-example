# coding: utf-8

import abc

import typing


class Command(metaclass=abc.ABCMeta):
    """
    Base command class
    """

    def add_arguments(self, parser) -> None:
        """
        add_arguments allow add arguments to subparser
        :param parser:
        :return:
        """
        pass

    @abc.abstractmethod
    def get_name(self) -> str:
        """
        This method must return name that will be used in CLI
        :return: name of command
        """
        pass

    def get_help(self) -> str:
        return ""

    @abc.abstractmethod
    def execute(self, opts: typing.Dict[typing.Any, typing.Any], args: typing.Any) -> None:
        """
        This method when actual work done
        :param opts: environment options
        :param args: CLI arguments
        :return: None
        """
        pass
