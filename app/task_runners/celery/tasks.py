# coding: utf-8
import typing

from core.business_logic import AddBusinessLogic


class AddTask:
    def __init__(self, add_business_logic: AddBusinessLogic) -> None:
        self.business_logic = add_business_logic

    def execute(self, first: typing.Union[int, float], second: typing.Union[int, float]) -> typing.Union[int, float]:
        return self.business_logic.execute(first=first, second=second)

    def get_task_func(self):
        def task(first: typing.Union[int, float], second: typing.Union[int, float]) -> typing.Union[int, float]:
            return self.execute(first, second)

        return task
