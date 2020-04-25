# coding: utf-8
from fastapi import FastAPI


class FastAPIInterface:
    """
    Example of API on  FastAPI framework
    """

    def __init__(self, task_runner):
        self.app = FastAPI()
        self.task_runner = task_runner

        # register class method as fast api handler
        # this allows us to use dependency injection
        self.app.post("/add")(self.add_items_post)

    def add_items_post(self, first: int, second: int) -> int:
        return self.task_runner.run_add_and_wait(first, second)
