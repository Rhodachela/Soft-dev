from rest_framework import serializers
from .models import Book, Teacher

from django.contrib.auth import get_user_model

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = ['id','title', 'author', 'author_name']

    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return data

class TeacherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
