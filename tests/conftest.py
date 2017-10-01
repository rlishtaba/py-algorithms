import random
from typing import List

import pytest


@pytest.fixture
def xs() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12, -1]


@pytest.fixture
def large_xs() -> List[int]:
    raw = [0, 6, 7, 8, 9, 4, 5, 12, -112] * 500
    random.shuffle(raw)
    return raw
