# coding: utf-8
from logging import config as logging_config


BROKER_URL = 'redis://localhost:6379/0'
RESULT_BACKEND_URL = 'redis://localhost:6379/0'

GRPC_PORT = "5555"
GRPC_WORKER_NUM = 10

config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple"
        }
    },
    "loggers": {
        "debug": {
            "level": "DEBUG",
            "handlers": ["console", ]
        },
        "grpc_server": {
            "level": "INFO",
            "handlers": ["console"],
        },
    }
}
logging_config.dictConfig(config)
