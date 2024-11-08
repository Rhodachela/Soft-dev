from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    description = models.TextField()
    no_of_employees = models.IntegerField()

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
         on_delete=models.SET_NULL,
         null=True, 
         related_name= "employees")
    #For Employee.department, I set on_delete=models.SET_NULL with null=True. 
    # This keeps an employee record even if their department is deleted, setting their department to NULL.

departments = Department.objects.prefetch_related("employees").all()


class Description(models.Model):
    content = models.TextField()

class Product(models.Model):
    prod_name = models.CharField(max_length=100, db_index=True)
    expiry_date = models.DateField()
    description = models.OneToOneField(
        Description, 
        on_delete=models.CASCADE)
    #Adding indexes (e.g., on fields frequently queried, like prod_name) can enhance performance if the dataset grows large. 

products = Product.objects.select_related("description").all()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length= 100)
    year_of_study =  models.DateField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(
        Students, 
        related_name="courses")

courses = Course.objects.prefetch_related("students").all()


