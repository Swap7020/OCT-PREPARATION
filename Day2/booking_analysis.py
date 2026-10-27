import numpy as np
import pandas as pd

data = {
    "booking_id": [1, 2, 3, 4, 5],
    "status": [
        "completed", "pending", "completed",
        "cancelled", "completed"
    ],
    "fare": [200, 150, 300, 100, 250]
}

df = pd.DataFrame(data)

print("Average fare:", df["fare"].mean())
print("\nBookings by status:")
print(df["status"].value_counts())

print("\nTotal fare by status:")
print(df.groupby("status")["fare"].sum())

fares = np.array([200, 150, 300, 100, 250])
print("\nFares above 200:", fares[fares > 200])
## data analysis on bookings 
print('median fare:', df['fare'].median())
print('completed bookings:', df[df["status"]=='completed']['booking_id'].count())
print('average fare:', df[df["status"]=='completed']['fare'].mean())