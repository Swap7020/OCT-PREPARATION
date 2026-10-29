def calculate_fare(
    distance_km: float,
    base_fare: float = 50,
    rate_per_km: float = 15
) -> float:
    if distance_km <= 0:
        raise ValueError("Distance must be positive")

    if base_fare < 0 or rate_per_km < 0:
        raise ValueError("Fare rates cannot be negative")

    return round(base_fare + distance_km * rate_per_km, 2)


print(calculate_fare(10))