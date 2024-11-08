from django.db import models
from users.models import User

# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField(max_length= 300)
    content = models.URLField()
    created = models.DateTimeField(auto_now_add= True)
    uploaded_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "uploads")
    thumbnail = models.URLField()

user1 = User()
upload1 = Upload(uploaded_by= user1)

user1.uploads
