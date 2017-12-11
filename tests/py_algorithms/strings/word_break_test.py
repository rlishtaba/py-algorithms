from py_algorithms.strings.word_break import WordBreak


class TestWordBreak:
    def test_apply(self):
        impls = [WordBreak.apply, WordBreak.dp_apply, WordBreak.dp2_apply]
        voc = ["cat", "cats", "and", "sand", "dog"]
        for impl in impls:
            is_possible = impl('catsanddog', voc)
            assert is_possible is True
