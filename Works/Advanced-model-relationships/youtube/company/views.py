from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellow_view(request):
    return HttpResponse("Hello world")

def book_list(request):
    books = Book.objects.all()
    context = {
        "book_list": books
    }
    return render(request, "books/book_list.html", context)

from django.views.generic import TemplateView

class Hello_view(TemplateView):
    template_name = "hello.html"


##Example 1
#This example shows a BookDetailView that inherits from DetailView and displays details of a specific book.
#  It overrides the get_context_data method to inject additional context data relevant to the book, such as its average rating (assuming a method get_average_rating exists on the Book model).
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Employee 

class EmployeesDetailView(DetailView):
    model = Employee
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee1 = Employee.get_object()
        context["avarage_rating"] = employee1.get_average_rating

#Example 2
#This example shows a BookUpdateView that inherits from UpdateView and facilitates updating details of a book. 
# It defines the editable fields (title, author, and description) and the template used for the update form (book_update_form.html). 
# It also sets the success_url to redirect the user to the book list view (book_list) after a successful update. 
# Additionally, it overrides the form_valid method to potentially execute custom logic after the form is validated (e.g., sending notifications).

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ["title", "author", "description"]
    template_name = "books/book_detail.html"
    success_url = reverse_lazy(book_list)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def display_message(request):
    return HttpResponse("Hellow world!")
    