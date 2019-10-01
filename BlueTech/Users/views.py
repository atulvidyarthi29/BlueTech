from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'home/homepage.html')


def dashboard(request):
    return render(request, 'home/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            login_user = authenticate(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password1'], )
            login(request, login_user)
            return redirect('users:dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
