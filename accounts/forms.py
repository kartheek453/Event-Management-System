from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class ClientRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "name",
            "email",
            "phone",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.ROLE_CLIENT
        user.email = self.cleaned_data["email"]
        user.name = self.cleaned_data.get("name", "")
        if commit:
            user.save()
        return user


class OrganizerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "name",
            "email",
            "phone",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.ROLE_ORGANIZER
        user.email = self.cleaned_data["email"]
        user.name = self.cleaned_data.get("name", "")
        if commit:
            user.save()
        return user