# coding: utf-8
from config import env
from .base import *

BROKER_URL = env.str("APP_BROKER_URL", "")
RESULT_BACKEND_URL = env.str("APP_RESULT_BACKEND_URL", "")

GRPC_PORT = env.str("APP_GRPC_PORT", GRPC_PORT)
GRPC_WORKER_NUM = env.int("APP_GRPC_WORKER_NUM", GRPC_WORKER_NUM)
