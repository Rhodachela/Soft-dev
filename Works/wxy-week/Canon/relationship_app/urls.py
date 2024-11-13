from django.urls import path
from .views import views

urlpatterns = [
    path('books/', views.list_all_books, name= "list_books"),
    parh('library/', views.LibraryDetailView.as_view(template_name= "library_detail")),
]