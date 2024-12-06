from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Book, Author, Librarian, Library
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import Bookform

# Create your views here.
def list_all_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {"form": form})

def home(request):
    return render(request, "relationship_app/home.html")

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

class CustomLogoutView(LogoutView):
    template_name= "relationship_app/logout"

#HELPER FUNCTIONS TO CHECK THE ROLES
def is_admin(user):
    return user.is_authenticated and user.userprofile.role =="Admin"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role =="Librarian"

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"

#Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {'role': 'Admin'})

#Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {'role': 'Librarian'})

#Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship-app/member_view.html", {"role": "Member"})

#View to add a new book
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method =="POST":
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = Bookform()
    return render(request, "relationship_app/add_book.html", {"form": form})

#View to edit an existing book
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = Bookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = Bookform()
        return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

#view to delete
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "relationship_app/delete_book.html", {"book": book})
