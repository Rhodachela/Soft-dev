from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email required")
        
        # Normalize the email and create user
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set is_staff and is_superuser to True for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager

# # Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self, email, password ):
#         if not email:
#             raise ValueError("Email required")
#         if self.model.objects.filter(email=email).exists():
#             raise ValueError("A user with this email already exists.")
#         user = self.model(email=self.normalize_email)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(self._db)
#         return user

# class User(AbstractUser):
#     email = models.EmailField(unique=True, max_length=255)
#     username = models.CharField(unique=False, max_length=50)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

