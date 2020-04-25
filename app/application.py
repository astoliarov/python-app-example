# coding: utf-8
import config

from task_runners.celery.runner import CeleryTaskRunner
from api.fastapi.api import FastAPIInterface


class Application:

    def __init__(self):
        self.task_runner = CeleryTaskRunner(config.BROKER_URL, config.RESULT_BACKEND_URL)
        self.interface = FastAPIInterface(self.task_runner)
