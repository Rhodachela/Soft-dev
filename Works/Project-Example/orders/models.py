from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here.
User = get_user_model()

ORDER_STATUSES = (
    ("pending", "Pending"),
    ("Completed", "Completed"),
    ("Delivered", "Delivered"),
)


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="orders")
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=None, related_name="orders")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUSES, default="Pending")
