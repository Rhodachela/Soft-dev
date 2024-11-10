from django.shortcuts import render

# Create your views here.


def my_home(request):
    return render(request, "base.html")
def blog(request):
    return render(request, "blog.html")
def contact(request):
    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")
def home(request):
    user_data = {
        "name": "Desmond Rono",
        "age": 26,
        "bio": " Engineer!",
        "hobbies": ["Playing Ps", "Swimming", "dancing"]
    }
    return render(request, "home.html", user_data)