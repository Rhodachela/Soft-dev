from django.urls import path
from . import views
from .views import my_home, blog, contact, about, home 
app_name = "users"


urlpatterns = [
    # path("R.chela/", view = welcome, name = "R.chela" ),
    path('home/', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('blog/', views.blog, name = "blog"),
    path('', views.my_home, name = "R.chela")
]