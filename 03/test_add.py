from main import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    assert add(-2, 3) == 1


def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
