# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

# Define the home page for logged-in users
def home(request):
    return render(request, "accounts/home.html")  # Change this to an actual home page

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = False
    success_url = reverse_lazy('home')
