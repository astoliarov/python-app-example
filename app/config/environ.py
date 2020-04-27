# coding: utf-8
from config import env
from .base import *

BROKER_URL = env.str("APP_BROKER_URL", "")  # type: ignore
RESULT_BACKEND_URL = env.str("APP_RESULT_BACKEND_URL", "")  # type: ignore

GRPC_PORT = env.str("APP_GRPC_PORT", GRPC_PORT)  # type: ignore
GRPC_WORKER_NUM = env.int("APP_GRPC_WORKER_NUM", GRPC_WORKER_NUM)  # type: ignore
