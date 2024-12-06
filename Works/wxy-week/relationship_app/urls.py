from django.urls import path
from .models import Book, Librarian, Library, Author
from .import views
from .views import CustomLoginView, register, CustomLogoutView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import admin_view, librarian_view, member_view
from .views import add_book, delete_book, edit_book

urlpatterns = [
    path('books/', views.list_all_books, name= "booklist"),
    path('librarydetail/<int:pk>/', views.LibraryDetailView.as_view(), name="library_detail"),
    path('register/',views.register, name= "register" ),
    path('home/', views.home, name="home"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('admin/', admin_view, name="admin_view"),
    path('librarian/', librarian_view, name="librarian_view"),
    path('member/', member_view, name="member_view"),
    path('add_book/', add_book, name="add_book"),
    path('edit_book', edit_book, name="edit_book"),
    path('delete_book/', delete_book, name="delete_book")
]
