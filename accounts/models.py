from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CLIENT = "CLIENT"
    ROLE_ORGANIZER = "ORGANIZER"
    ROLE_MANAGER = "MANAGER"

    ROLE_CHOICES = (
        (ROLE_CLIENT, "Client"),
        (ROLE_ORGANIZER, "Organizer"),
        (ROLE_MANAGER, "Manager"),
    )

    name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_CLIENT)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def is_client(self):
        return self.role == self.ROLE_CLIENT

    def is_organizer(self):
        return self.role == self.ROLE_ORGANIZER

    def is_manager(self):
        return self.role == self.ROLE_MANAGER

    def __str__(self):
        return self.name or self.username