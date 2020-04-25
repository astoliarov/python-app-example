# coding: utf-8
from celery import Celery

from .tasks import task_add


class CeleryTaskRunner:

    def __init__(self, broker_url: str, result_backend_url: str) -> None:
        self.broker_url = broker_url
        self.app = Celery('tasks', broker=broker_url, backend=result_backend_url)
        self._register_tasks()

    def _register_tasks(self):
        self.add_task = self.app.task(task_add)

    def run_add(self, first: int, second: int) -> None:
        self.add_task.delay(first, second)

    def run_add_and_wait(self, first: int, second: int) -> int:
        task = self.add_task.delay(first, second)
        return task.wait(timeout=None, interval=0.5)
