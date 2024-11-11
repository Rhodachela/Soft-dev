from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    email = models.EmailField()

# #Create user
# user = User.objects.create_user("John Doe", "john@gmail.com", "password123")

# # Retrieve a user based on username
# user = User.objects.get(username="John")

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"
