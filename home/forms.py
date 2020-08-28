from django import forms

class UserQuestion(forms.Form):
    question = forms.CharField(label= "recherchez un aliment", max_length=100)
