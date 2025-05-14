import pytest
from main import add, sub, div


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(-2, 3) == 1

    def test_add_with_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    def test_add_with_string(self):
        with pytest.raises(ValueError):
            add("0", 5)


# def test_sub_testing():
#     assert sub(1, 2) == -1


# def test_div_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(1, 0)

#     assert div(0, 1) == 0
