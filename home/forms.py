from django import forms


class UserQuestion(forms.Form):
    question = forms.CharField(max_length=100)
