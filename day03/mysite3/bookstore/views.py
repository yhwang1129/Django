from django.shortcuts import render
from .models import Book

# Create your views here.
def all_books(request):

    books = Book.objects.all()

    return render(request, 'bookstore/all_book.html', locals())