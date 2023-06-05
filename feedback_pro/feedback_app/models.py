from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    email = models.EmailField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=timezone.now())
    description = models.CharField(max_length=255)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.email