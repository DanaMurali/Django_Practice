from rest_framework import serializers
from demo.models import Book, BookNumber, Character

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

# we create class and then pass in built in django methods and then we are saying we want to use our mode Book and then use title
class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'published', 'is_published', 'number', 'characters']