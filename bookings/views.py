from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import client_required, manager_required, organizer_required
from .forms import BookingForm, ManagerBookingForm, OrganizerBookingForm
from .models import Booking
from events.models import Event


@login_required
@client_required
def schedule_booking(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            payment_status = request.POST.get("payment_status", "PENDING")
            booking = form.save(commit=False)
            booking.client = request.user
            booking.event = event
            booking.payment_status = "PAID" if payment_status == "PAID" else "PENDING"
            booking.booking_status = "PENDING"
            booking.save()
            if payment_status == "PAID":
                messages.success(request, "Booking created and payment marked as Paid.")
            else:
                messages.success(request, "Booking created. Your payment is pending.")
            return redirect("client_bookings")
    else:
        form = BookingForm()
    return render(request, "bookings/booking_form.html", {"form": form, "event": event})


@login_required
@client_required
def client_bookings(request):
    bookings = Booking.objects.filter(client=request.user).order_by("-created_at")
    return render(request, "bookings/client_bookings.html", {"bookings": bookings})


@login_required
@manager_required
def manager_bookings(request):
    bookings = Booking.objects.all().order_by("-created_at")
    return render(request, "bookings/manager_bookings.html", {"bookings": bookings})


@login_required
@manager_required
def manage_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = ManagerBookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.booking_status == "REJECTED" and not booking.rejection_reason:
                form.add_error("rejection_reason", "Please add a rejection reason.")
            else:
                booking.save()
                messages.success(request, "Booking updated successfully.")
                return redirect("manager_bookings")
    else:
        form = ManagerBookingForm(instance=booking)
    return render(request, "bookings/manage_booking.html", {"form": form, "booking": booking})


@login_required
@organizer_required
def organizer_bookings(request):
    bookings = Booking.objects.filter(organizer=request.user).order_by("event_date")
    return render(request, "bookings/organizer_bookings.html", {"bookings": bookings})


@login_required
@organizer_required
def organizer_update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, organizer=request.user)
    if request.method == "POST":
        form = OrganizerBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking status updated.")
            return redirect("organizer_bookings")
    else:
        form = OrganizerBookingForm(instance=booking)
    return render(request, "bookings/organizer_update_booking.html", {"form": form, "booking": booking})


def complete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.booking_status = "COMPLETED"
        booking.save()
        messages.success(request, "Booking marked as completed.")
    return redirect("public_organizer_dashboard")

