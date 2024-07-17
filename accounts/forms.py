# accounts/views.py or wherever you need to import these forms

from django import forms
from book_app.forms import AuthorForm, BookForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
