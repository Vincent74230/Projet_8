from django.shortcuts import render
from . forms import UserQuestion, RegisterForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    QuestionForm = UserQuestion()
    Registration = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
    context = {'QuestionForm':QuestionForm, 'RegisterForm':Registration}
    return render(request, 'user_account/index.html', context)
