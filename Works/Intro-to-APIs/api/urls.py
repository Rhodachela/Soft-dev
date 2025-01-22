from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('list/', BookList.as_view(), name = 'Book-List'), #Maps to the book list view
    path('', include(router.urls)), #This includes all routes registered with the router
    path('api-token-auth/', obtain_auth_token, name = 'api-token-auth'), #Token retrieval endpoint

]