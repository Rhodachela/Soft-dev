from .models import Book, Author, Librarian, Library

def get_book_by_author(author_name):
    try:
        author = Author.objects.get(name = author_name)
        books = Book.objects.all()
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None
    
def list_all_books(library_name):
    try:
        library = Library.objects.get(name= library_name)
        books = Library.libraries.all()
        return books
    except Library.DoesNotExist:
        return None

def retrieve_librarian(library_name):
    try:
        library = Library.objects.get(name = library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
