import pytest
from fare_service import calculate_fare


def test_valid_distance_returns_200():
    assert calculate_fare(10) == 200


def test_zero_distance_raises_error():
    with pytest.raises(ValueError):
        calculate_fare(0)


def test_negative_distance_raises_error():
    with pytest.raises(ValueError):
        calculate_fare(-5)