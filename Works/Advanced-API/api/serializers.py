from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, publication_year):
        if publication_year > datetime.now().year:
            raise serializers.ValidationError("Publication Year cannot be in the future")
        return publication_year


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
