
class Booking:
    VALID_STATUSES = {"pending", "completed", "cancelled"}

    def __init__(self, booking_id, customer_name, status="pending"):
        if not isinstance(booking_id, int) or isinstance(booking_id, bool) or booking_id <= 0:
            raise ValueError("Booking ID must be a positive integer")
        
        if not isinstance (customer_name, str) or  not customer_name.strip():
            raise ValueError("Customer name cannot be empty")

        if status not in self.VALID_STATUSES:
            raise ValueError("Invalid booking status")

        self.booking_id = booking_id
        self.customer_name = customer_name.strip()
        self.status = status

    def update_status(self, new_status):
        if new_status not in self.VALID_STATUSES:
            raise ValueError("Invalid booking status")

        self.status = new_status

    def cancel_booking(self):
        if self.status== 'completed':
            raise ValueError('completed bookings cannot be cancelled')

        if self.status=='cancelled':
            raise ValueError('Booking already cancelled')

        self.status= "cancelled"


    def display_details(self):
        return {
            "booking_id": self.booking_id,
            "customer_name": self.customer_name,
            "status": self.status
        }


booking = Booking(101, "Rahul")
booking.update_status("completed")

print(booking.display_details())