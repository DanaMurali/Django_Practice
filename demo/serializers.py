from rest_framework import serializers
from demo.models import Book

# we create class and then pass in built in django methods and then we are saying we want to use our mode Book and then use title
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'published', 'is_published']