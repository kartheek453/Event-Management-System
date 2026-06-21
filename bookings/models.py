from django.db import models
from accounts.models import User
from events.models import Event


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = (
        ("PENDING", "Pending Approval"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("COMPLETED", "Completed"),
    )

    PAYMENT_CHOICES = (
        ("PAID", "Paid"),
        ("PENDING", "Pending"),
    )

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="client_bookings",
    )
    organizer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="organizer_bookings",
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    requirements = models.TextField(blank=True)
    booking_status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS_CHOICES,
        default="PENDING",
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default="PENDING",
    )
    rejection_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} - {self.event.title}"
