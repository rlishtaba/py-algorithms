import pytest

from py_algorithms.dynamic_connectivity import dynamic_connectivity_brute_force


@pytest.fixture
def payload():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestDynamicConnectivity:
    def testBruteForce(self):
        impl = dynamic_connectivity_brute_force(payload())

        assert impl.is_connected(0, 9) is False
        impl.connect(0, 9)
        assert impl.is_connected(0, 9) is True

        assert impl.is_connected(0, 1) is False
        impl.connect(0, 1)
        assert impl.is_connected(0, 9) is True

        assert impl.is_connected(5, 8) is False
        impl.connect(5, 8)
        assert impl.is_connected(5, 8) is True

        assert impl.is_connected(9, 8) is False
        impl.connect(9, 8)
        assert impl.is_connected(9, 8) is True

        # Transitivity rule
        assert impl.is_connected(5, 9) is True
