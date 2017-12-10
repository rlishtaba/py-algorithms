__all__ = [
    'new_circular_array'
]

from .circular_array import CircularArray


def new_circular_array(size: int = 5) -> CircularArray:
    """
    Factory method
    :param size: initial array size
    :return: CircularArray
    """
    return CircularArray(size)
