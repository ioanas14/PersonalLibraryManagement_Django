from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from library_management_app.models import Books

def showDemoPage(request):
    return render(request, "demo.html")

def showHomePage(request):
    return render(request, "home.html")

# def showBooksPage(request):
#     return render(request, "books.html")

def showAddBook(request):
    return render(request, "addBook.html")

def addBook(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        try:
            newBook = Books()
            newBook.name = request.POST.get("bookName")
            newBook.author = request.POST.get("bookAuthor")
            newBook.type = request.POST.get("bookType")
            newBook.save()
            return HttpResponseRedirect("/addBook")
        except:
            return HttpResponseRedirect("/addBook")

def viewBooks(request):
    books = Books.objects.all()
    return render(request, "books.html", {'book':books})