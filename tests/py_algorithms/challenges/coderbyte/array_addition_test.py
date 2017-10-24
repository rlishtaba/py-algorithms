from py_algorithms.challenges.coderbyte.array_addition import ArrayAddition


class ArrayAdditionTest:
    def test_impl(self):
        inputs = {
            True: [4, 6, 23, 10, 1, 3],
            False: [4, 6, 123, 10, 1, 3]
        }
        f = ArrayAddition()
        for key in inputs:
            assert f(inputs[key]) == key
