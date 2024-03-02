from django.db import models

# Create your models here.

class Student(models.Model):
       fullname   = models.CharField(max_length=255)
       hallticket = models.CharField(max_length=255)
       clgname    = models.CharField(max_length=255)
       amount     = models.CharField(max_length=255)
       mobile     = models.CharField(max_length=255)
