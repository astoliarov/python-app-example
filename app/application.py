# coding: utf-8
import config
from api.grpc.server import GRPCInterface

from core.business_logic import AddBusinessLogic, DelayedAddBusinessLogic

from task_runners.celery.runner import CeleryTaskRunner
from api.fastapi.api import FastAPIInterface
from cli.custom import init_cli


class Application:
    def __init__(self):
        self.add_bl = AddBusinessLogic()

        self.task_runner = CeleryTaskRunner(config.BROKER_URL, config.RESULT_BACKEND_URL, self.add_bl)

        self.delayed_add_bl = DelayedAddBusinessLogic(self.task_runner)

        self.interface = FastAPIInterface(self.delayed_add_bl)
        self.grpc_interface = GRPCInterface(self.delayed_add_bl, config.GRPC_PORT, config.GRPC_WORKER_NUM)
        self.cli = init_cli("basic app CLI", self)
