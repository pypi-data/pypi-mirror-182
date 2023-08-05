"""Entry point for pydantic-aioredis"""
# set by poetry-dynamic-versioning
__version__ = "1.1.1"  # noqa: E402

from .config import RedisConfig  # noqa: F401
from .model import Model  # noqa: F401
from .store import Store  # noqa: F401
