import math


def validate_features(features):
    if not isinstance(features, int) or isinstance(features, bool):
        raise ValueError("Features must be an integer")

    if features < 30:
        raise ValueError("At least 30 features are required")

    return 200