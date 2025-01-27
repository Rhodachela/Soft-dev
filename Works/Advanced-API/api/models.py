from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} By {self.author}"

    def clean(self):
        # Add custom validation logic
        if self.publication_year > datetime.now().year:
            raise ValidationError({'publication_year': "Publication Year cannot be in the future"})
