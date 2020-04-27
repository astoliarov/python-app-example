# coding: utf-8
from core.business_logic import AddBusinessLogic


class AddTask:
    def __init__(self, add_business_logic: AddBusinessLogic) -> None:
        self.business_logic = add_business_logic

    def execute(self, first: int, second: int) -> int:
        return self.business_logic.execute(first=first, second=second)

    def get_task_func(self):
        def task(first: int, second: int) -> int:
            return self.execute(first, second)

        return task
