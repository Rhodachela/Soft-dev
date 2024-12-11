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
        fields = ["title", "content", "author", "created_at"]

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.usename", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

class BlogPostSerializer(serializers.ModelSerializer):
    Comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"

    def validate(self, data):
        if len(data[title]) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return data

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["email", "username", "first_name", "last_name", "full_name" ]

        def get_full_name(self, obj):
            return f"{obj.first_name} {obj.last_name}" if obj.first_name and obj.last_name else obj.username