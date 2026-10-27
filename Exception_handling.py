def calculate_fare(distance_km: float, rate: float=15) -> float:
    if distance_km <=0:
        raise ValueError("Distance must be greater than zero")

    return 50 + distance_km * rate

try:
    fare = calculate_fare(10)
    print(f'Estimated fare: {fare:.2f}')

except ValueError as error:
    print(f'Invalid booking:{error}')
