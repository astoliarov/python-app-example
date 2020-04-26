# coding: utf-8
from fastapi import FastAPI

from core.business_logic import DelayedAddBusinessLogic


class FastAPIInterface:
    """
    Example of API on  FastAPI framework
    """

    def __init__(self, delayed_add_bl: DelayedAddBusinessLogic):
        self.app = FastAPI()
        self.delayed_add_bl = delayed_add_bl

        # register class method as fast api handler
        # this allows us to use dependency injection
        self.app.post("/add")(self.add_items_post)

    def add_items_post(self, first: int, second: int) -> int:
        return self.delayed_add_bl.execute(first, second)
