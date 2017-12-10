from py_algorithms.stacks.finding_spans import FindingSpans


class TestFindingSpans:
    def test_apply(self):
        data = [6, 3, 4, 5, 2, 3, 2, 1, 0, 0]
        spans = FindingSpans.apply(data)
        assert spans == [1, 1, 2, 3, 1, 2, 1, 1, 1, 1]
