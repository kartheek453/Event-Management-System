from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("event", "client", "organizer", "booking_status", "payment_status", "event_date")
    list_filter = ("booking_status", "payment_status", "event_date")
    search_fields = ("client__username", "event__title", "organizer__username")
