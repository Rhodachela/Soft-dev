from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import Permission

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("Password required!")
        
        user = self.model(email = self.normalize_email(email))   
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(BaseUserManager):
        user.is_staff = True
        user.is_superuser = True
        user = self.create_user(email, password)
        user.save(using=self._db)

        return user

class CustomUser(AbstractUser):
    bio = models.CharField(blank=True)
    username = None
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    USERNAME_FIELD = email
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

def my_view(request):
    if request.user.has_perm('Can_add_book'):
        ...
    else:
        # Deny access or show an error message
        ...

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Implement logic to authenticate user using email and password
        ...
    def get_user(self, user_id):
        # Implement logic to retrieve user based on user ID
        ...

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publication_year = models.IntegerField(null=True, blank=True)

    class Meta:
        Permissions = [
            ("can_view", ("Can view book")),
            ("can_create_book", ("Can create a new book")),
            ("can_edit_book", ("Can change the book format")),
            ("can_delete_book", ("Can delete books")),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255, default="Default location")
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarians")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofiles")
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwags):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwags):
    instance.UserProfile.save()
    