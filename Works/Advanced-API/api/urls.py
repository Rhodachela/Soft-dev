from django.urls import path
from .views import (
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
    BookCreateView
)

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/', BookListView.as_view(), name = 'book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]