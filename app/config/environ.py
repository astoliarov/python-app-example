# coding: utf-8
from config import env
from .base import *

BROKER_URL = env.str("APP_BROKER_URL", "")
RESULT_BACKEND_URL = env.str("APP_RESULT_BACKEND_URL", "")
