import pytest
from scratch import average_rating

def test_average_normal():
    assert average_rating([4, 5, 3]) == 4.0

def test_average_empty():
    result = average_rating([])
    assert result == 0
