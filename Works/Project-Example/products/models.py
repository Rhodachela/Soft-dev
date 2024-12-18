from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products") #category.products
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", default=None, null=True)#user.products
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    