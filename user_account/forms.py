from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserQuestion(forms.Form):
    question = forms.CharField(label= "Recherchez un aliment", max_length=100)

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(label='Prénom', max_length=100)
    last_name=forms.CharField(label='Nom', max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
