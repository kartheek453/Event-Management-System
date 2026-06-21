from django import forms
from accounts.models import User
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["event_date", "event_time", "location", "requirements"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "event_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "requirements": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class ManagerBookingForm(forms.ModelForm):
    organizer = forms.ModelChoiceField(
        queryset=User.objects.filter(role=User.ROLE_ORGANIZER),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Booking
        fields = ["booking_status", "organizer", "rejection_reason"]
        widgets = {
            "booking_status": forms.Select(attrs={"class": "form-select"}),
            "rejection_reason": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }


class OrganizerBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking_status"]
        widgets = {
            "booking_status": forms.Select(attrs={"class": "form-select"}),
        }
