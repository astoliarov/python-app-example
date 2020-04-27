# coding: utf-8
from celery import Celery

from core.business_logic import AddBusinessLogic
from core.interfaces import ITaskRunner

from .tasks import AddTask


class CeleryTaskRunner(ITaskRunner):
    def __init__(self, broker_url: str, result_backend_url: str, add_business_logic: AddBusinessLogic) -> None:
        self.add_business_logic = add_business_logic
        self.broker_url = broker_url
        self.app = Celery("tasks", broker=broker_url, backend=result_backend_url)

        self.add_task = self.app.task(AddTask(self.add_business_logic).get_task_func())

    def run_add(self, first: int, second: int) -> None:
        self.add_task.delay(first, second)

    def run_add_and_wait(self, first: int, second: int) -> int:
        task = self.add_task.delay(first, second)
        return task.wait(timeout=None, interval=0.5)
