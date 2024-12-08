from django.urls import path, include
from .serializers import BookSerializer
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all/', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name="book_list"),
    path('', include(router.urls))
    ]