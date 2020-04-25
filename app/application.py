# coding: utf-8
import config

from task_runners.celery.runner import CeleryTaskRunner


class Application:

    def __init__(self):
        self.task_runner = CeleryTaskRunner(config.BROKER_URL, config.RESULT_BACKEND_URL)
