# coding: utf-8

from application import Application
# import of tasks to allow celery find them
from .tasks import task_add

app_instance = Application()

app = app_instance.task_runner.app
