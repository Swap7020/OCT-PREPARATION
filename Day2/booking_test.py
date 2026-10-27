
import unittest
from Day1.booking import Booking


class TestBooking(unittest.TestCase):

    def test_valid_booking(self):
        booking = Booking(101, "Rahul")
        self.assertEqual(booking.booking_id, 101)
        self.assertEqual(booking.status, "pending")

    def test_invalid_booking_ids(self):
        for booking_id in [0, -1, 1.5, "101", True]:
            with self.subTest(booking_id=booking_id):
                with self.assertRaises(ValueError):
                    Booking(booking_id, "Rahul")

    def test_empty_customer_name(self):
        for name in ["", "   "]:
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    Booking(101, name)

    def test_invalid_initial_status(self):
        with self.assertRaises(ValueError):
            Booking(101, "Rahul", "processing")

    def test_update_status(self):
        booking = Booking(101, "Rahul")
        booking.update_status("completed")
        self.assertEqual(booking.status, "completed")

    def test_invalid_updated_status(self):
        booking = Booking(101, "Rahul")
        with self.assertRaises(ValueError):
            booking.update_status("processing")

    def test_cancel_booking(self):
        booking = Booking(101, "Rahul")
        booking.cancel_booking()
        self.assertEqual(booking.status, "cancelled")

    def test_cancel_completed_booking(self):
        booking = Booking(101, "Rahul", "completed")
        with self.assertRaises(ValueError):
            booking.cancel_booking()

    def test_cancel_twice(self):
        booking = Booking(101, "Rahul")
        booking.cancel_booking()
        with self.assertRaises(ValueError):
            booking.cancel_booking()


if __name__ == "__main__":
    unittest.main()
