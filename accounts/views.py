from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from bookings.models import Booking
from accounts.decorators import client_required, manager_required, organizer_required
from .forms import ClientRegisterForm, OrganizerCreationForm
from .models import User


def profile(request):
    return render(request, "accounts/profile.html")


def client_access(request):
    return render(request, "accounts/client_access.html")


def role_login(request, role):
    role_label = {
        User.ROLE_CLIENT: "Client",
        User.ROLE_ORGANIZER: "Organizer",
        User.ROLE_MANAGER: "Manager",
    }.get(role, "User")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.role != role:
                form.add_error(None, f"Please login with a {role_label} account.")
            else:
                login(request, user)
                if role == User.ROLE_CLIENT:
                    return redirect("event_list")
                if role == User.ROLE_ORGANIZER:
                    return redirect("organizer_dashboard")
                if role == User.ROLE_MANAGER:
                    return redirect("manager_dashboard")
    else:
        form = AuthenticationForm(request)
    form.fields["username"].label = "Email"
    return render(request, "accounts/login.html", {"form": form, "role_label": role_label})


def client_register(request):
    if request.method == "POST":
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Client account created successfully.")
            return redirect("event_list")
    else:
        form = ClientRegisterForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
@client_required
def client_dashboard(request):
    bookings = Booking.objects.filter(client=request.user).order_by("-created_at")
    return render(request, "accounts/client_dashboard.html", {"bookings": bookings})


@login_required
@manager_required
def manager_dashboard(request):
    bookings = Booking.objects.all()
    total_bookings = bookings.count()
    approved_bookings = bookings.filter(booking_status="APPROVED").count()
    rejected_bookings = bookings.filter(booking_status="REJECTED").count()
    completed_bookings = bookings.filter(booking_status="COMPLETED").count()
    paid_amount = sum([booking.event.price for booking in bookings if booking.payment_status == "PAID"])
    pending_amount = sum([booking.event.price for booking in bookings if booking.payment_status == "PENDING"])
    return render(
        request,
        "accounts/manager_dashboard.html",
        {
            "total_bookings": total_bookings,
            "approved_bookings": approved_bookings,
            "rejected_bookings": rejected_bookings,
            "completed_bookings": completed_bookings,
            "paid_amount": paid_amount,
            "pending_amount": pending_amount,
        },
    )


@login_required
@manager_required
def create_organizer(request):
    if request.method == "POST":
        form = OrganizerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Organizer account created successfully.")
            return redirect("manager_dashboard")
    else:
        form = OrganizerCreationForm()
    return render(request, "accounts/create_organizer.html", {"form": form})


@login_required
@organizer_required
def organizer_dashboard(request):
    bookings = Booking.objects.filter(organizer=request.user).order_by("event_date")
    return render(request, "accounts/organizer_dashboard.html", {"bookings": bookings})


def public_organizer_dashboard(request):
    bookings = Booking.objects.filter(booking_status="APPROVED").order_by("event_date")
    return render(request, "accounts/public_organizer_dashboard.html", {"bookings": bookings})

