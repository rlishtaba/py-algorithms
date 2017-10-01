from typing import Any


def three_way_cmp(a: Any, b: Any) -> int:
    """Three-Way Comparison takes two values A and B belonging to a type
        with a total order and determines whether A < B, A = B, or A > B in a
        single operation, in accordance with the mathematical law of trichotomy.
    """
    return (a > b) - (a < b)


def test_iterable(xs: Any):
    if not isinstance(xs, (list, tuple)):
        raise RuntimeError('Can sort only iterable entity.')
