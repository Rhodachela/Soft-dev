from rest_framework import serializers
from .models import Book
from datetime import date, timezone
from my_app.models import Post

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "name", "author"]

    def validate(self, data):
        if len(data["name"]) <5:
            raise serializers.ValidationError("Name must be a character of 5")
        return data

    def get_days_since_created(self, obj):
        return (date.today()-obj.created_at_date()).days

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at"]