from environs import Env

from .base import *

env = Env()

if env.bool("STATS_ENV_CONFIG", False):
    from .environ import *
else:
    try:
        from .local import *
    except ImportError:
        pass
