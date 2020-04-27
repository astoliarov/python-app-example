# coding: utf-8

import logging
import signal
import time
from concurrent import futures

import grpc

from core.business_logic import DelayedAddBusinessLogic

from api.grpc import interface_pb2, interface_pb2_grpc

logger = logging.getLogger("grpc_server")


class Servicer(interface_pb2_grpc.InterfaceServicer):
    def __init__(self, delayed_add_bl: DelayedAddBusinessLogic):
        self.delayed_add_bl = delayed_add_bl

    def Add(self, request, context):
        logger.info(f"received request: {request}")
        result = self.delayed_add_bl.execute(request.first, request.second)

        response = interface_pb2.AddResponse(result=result)
        logger.info(f"sending response: {response}")
        return response


class GRPCInterface:

    def __init__(self, delayed_add_bl: DelayedAddBusinessLogic, port: str, max_worker_num: int):
        self.address = f"[::]:{port}"
        self.servicer = Servicer(delayed_add_bl)
        self.grpc_server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=max_worker_num)
        )
        interface_pb2_grpc.add_InterfaceServicer_to_server(self.servicer, self.grpc_server)

    def serve(self):
        self.grpc_server.add_insecure_port(self.address)
        self.grpc_server.start()

        is_working = True

        def signal_handler(signalNumber, frame):
            is_working = False

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGQUIT, signal_handler)

        logger.info(f"listening for requests on: {self.address}")
        while is_working:
            time.sleep(1)
