# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer, MiniBookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = MiniBookSerializer
    queryset = Book.objects.all()
    # have to pass in as a tuple so it doesn't take it as one value.
    authentication_classes = (TokenAuthentication,)
    # this overrides the settings.py where we say allow any
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


# Now we have a get function inside class
# class Another(View):
#
#     # we are selecting all the books here
#     books = Book.objects.all()
#     # books = Book.objects.filter(is_published=True)
#     # books = Book.objects.get(id=2) -> get only brings up one object
#
#     output = ''
#     # for each book we concatenate to the string for each book
#     for book in books:
#         output += f"We have {book.title} book with ID {book.id}<br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)

# render takes two arguments: request and the file path and can pass a third argument object
# we are passing an object and in that object is data which is a string
# def first(request):
#
#     books = Book.objects.all()
#     return render(request, 'first_temp.html', {'books':books})