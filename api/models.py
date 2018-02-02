from django.db import models

# Create your models here.
class Barcamp(models.Model):
    # fields
    title = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(unique=True)

class Speaker(models.Model):
    # fields
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Talk(models.Model):
    # relations
    barcamp = models.ForeignKey(Barcamp, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    # fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    slides_name = models.CharField(max_length=200, unique=True)

class Admin(models.Model):
    # fields
    email = models.EmailField(unique=True)
