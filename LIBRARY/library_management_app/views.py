from django.shortcuts import render


def showDemoPage(request):
    return render(request, "demo.html")

def showHomePage(request):
    return render(request, "home.html")

def showBooksPage(request):
    return render(request, "books.html")

def showAddBook(request):
    return render(request, "addBook.html")

