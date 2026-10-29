import pytest

from validation import validate_features

import pytest
from validation import validate_features


def test_valid_input_returns_200():
    assert validate_features(30) == 200


def test_less_than_30_features_raises_error():
    with pytest.raises(ValueError):
        validate_features(29)


def test_float_features_values_raises_error():
    with pytest.raises(ValueError):
        validate_features(30.5)