import json

booking = {
    "booking_id": 101,
    "status": "completed",
    "fare": 200
}

with open("booking.json", "w", encoding="utf-8") as file:
    json.dump(booking, file, indent=2)

with open("booking.json", "r", encoding="utf-8") as file:
    loaded_booking = json.load(file)

print(loaded_booking)