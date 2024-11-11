from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.register, name = "register"),
    path('home/', views.home, name = "home"),
    path('login/', CustomLoginView.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(template_name= "accounts/logout.html"), name = "logout"),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]