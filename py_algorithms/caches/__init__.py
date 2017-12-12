__all__ = [
    'new_lfu_cache',
    'new_lru_cache'
]

from .lfu_cache import LfuCache
from .lru_cache import LruCache


def new_lfu_cache(size) -> LfuCache:
    """
    Factory method
    :param size: Size of cache
    :return: LfuCache
    """
    return LfuCache(size)


def new_lru_cache(size) -> LruCache:
    """
    Factory method
    :param size: Size of cache
    :return: LruCache
    """
    return LruCache(size)
