from django.urls import path
from . import views

urlpatterns = [
    path("schedule/<int:event_id>/", views.schedule_booking, name="schedule_event"),
    path("client/", views.client_bookings, name="client_bookings"),
    path("manager/", views.manager_bookings, name="manager_bookings"),
    path("manager/<int:booking_id>/", views.manage_booking, name="manage_booking"),
    path("organizer/", views.organizer_bookings, name="organizer_bookings"),
    path("organizer/<int:booking_id>/", views.organizer_update_booking, name="organizer_update_booking"),
    path("complete/<int:booking_id>/", views.complete_booking, name="complete_booking"),
]
