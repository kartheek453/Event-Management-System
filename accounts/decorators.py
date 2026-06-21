from django.contrib.auth.decorators import user_passes_test
from .models import User


def client_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and user.role == User.ROLE_CLIENT,
        login_url="client_login",
    )(view_func)


def organizer_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and user.role == User.ROLE_ORGANIZER,
        login_url="organizer_login",
    )(view_func)


def manager_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and user.role == User.ROLE_MANAGER,
        login_url="manager_login",
    )(view_func)
