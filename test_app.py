from app import square, is_even


def test_square_positive_number():
    assert square(5) == 25


def test_square_negative_number():
    assert square(-4) == 16


def test_is_even_with_even_number():
    assert is_even(6) is True


def test_is_even_with_odd_number():
    assert is_even(7) is False