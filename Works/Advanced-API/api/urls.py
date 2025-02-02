from django.urls import path
from .views import (
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
    BookCreateView
)

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='book-create'), # Book creation view
    path('books/', BookListView.as_view(), name = 'book-list'), # Book list view
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # Book details view
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'), 
]