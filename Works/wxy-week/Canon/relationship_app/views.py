from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Librarian, Book, Author

# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"