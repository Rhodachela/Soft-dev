from django.shortcuts import render

# Create your views here.
def welcome(request):
    is_frontend = True

    books = [
        "First book", "Things fall apart", "Rich dad"
    ]
    context = {
        "name": "Ben henry",
        "books": books
    }


    if is_frontend:
        return render(request, "fe.html", context,)

    return render(request,"be.html", context,)
