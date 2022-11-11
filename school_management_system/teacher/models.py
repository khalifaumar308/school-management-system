from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Address(models.Model):
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=11)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=75, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    post = models.CharField(max_length=100, null=True)


class Class(models.Model):
    name = models.CharField(max_length=10, unique=True, db_index=True)
    department = models.CharField(max_length=50)
    form_master = models.OneToOneField(Teacher, on_delete=models.DO_NOTHING)


class Subject(models.Model):
    subject = models.CharField(max_length=50)
    teacher = models.ManyToManyField(Teacher)
    class_taken = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
