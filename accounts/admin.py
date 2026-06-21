from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Extra information", {"fields": ("name", "role", "phone")}),
    )
    list_display = ("username", "email", "name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")
