from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("client/access/", views.client_access, name="client_access"),
    path("client/login/", views.role_login, {"role": "CLIENT"}, name="client_login"),
    path("organizer/login/", views.role_login, {"role": "ORGANIZER"}, name="organizer_login"),
    path("organizer/bookings/", views.public_organizer_dashboard, name="public_organizer_dashboard"),
    path("manager/login/", views.role_login, {"role": "MANAGER"}, name="manager_login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("signup/", views.client_register, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("client/dashboard/", views.client_dashboard, name="client_dashboard"),
    path("organizer/dashboard/", views.organizer_dashboard, name="organizer_dashboard"),
    path("manager/dashboard/", views.manager_dashboard, name="manager_dashboard"),
    path("manager/create-organizer/", views.create_organizer, name="create_organizer"),
]
