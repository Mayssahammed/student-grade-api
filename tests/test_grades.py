import pytest

from src.grades import average


def test_average_of_two_grades():
    assert average([10, 20]) == 15.0


def test_average_of_single_grade():
    assert average([12]) == 12.0


def test_average_of_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])
