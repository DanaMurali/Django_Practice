from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.

# Now we have a get function inside class
class Another(View):

    # we are selecting all the books here
    books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    # books = Book.objects.get(id=2) -> get only brings up one object

    output = ''
    # for each book we concatenate to the string for each book
    for book in books:
        output += f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First message from views')