import pytest

from py_algorithms.data_structures import new_suffix_array


class TestStack:
    def test_suffix_array(self):
        ds = new_suffix_array('python')
        assert ds.is_sub_str('') is False
        assert ds.is_sub_str('p') is True
        assert ds.is_sub_str('py') is True
        assert ds.is_sub_str('pyt') is True
        assert ds.is_sub_str('pyth') is True
        assert ds.is_sub_str('pytho') is True
        assert ds.is_sub_str('python') is True
        assert ds.is_sub_str('ython') is True
        assert ds.is_sub_str('thon') is True
        assert ds.is_sub_str('hon') is True
        assert ds.is_sub_str('on') is True
        assert ds.is_sub_str('n') is True

    def test_an_empty_str_in_constructor(self):
        with pytest.raises(RuntimeError, match=r'Could not work with Nothing.'):
            new_suffix_array('')

    def test_an_empty_str_or_nothing_in_lookup(self):
        ds = new_suffix_array('python')
        assert ds.is_sub_str(None) is False
        assert ds.is_sub_str(1) is False

    def test_numeric_value(self):
        ds = new_suffix_array(1234567)
        assert ds.is_sub_str(1) is True
        assert ds.is_sub_str(12) is True
        assert ds.is_sub_str(123) is True
        assert ds.is_sub_str(1234) is True
        assert ds.is_sub_str(12345) is True
        assert ds.is_sub_str(123456) is True
        assert ds.is_sub_str(1234567) is True
        assert ds.is_sub_str(234567) is True
        assert ds.is_sub_str(34567) is True
        assert ds.is_sub_str(4567) is True
        assert ds.is_sub_str(567) is True
        assert ds.is_sub_str(67) is True
        assert ds.is_sub_str(7) is True
