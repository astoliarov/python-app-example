# coding: utf-8
import typing

from core.interfaces import ITaskRunner


class AddBusinessLogic:

    def execute(self, first: typing.Union[int, float], second: typing.Union[int, float]) -> typing.Union[int, float]:
        return first + second


class DelayedAddBusinessLogic:

    def __init__(self, task_runner: ITaskRunner):
        self.task_runner = task_runner

    def execute(self, first: int, second: int) -> int:
        return self.task_runner.run_add_and_wait(first=first, second=second)
