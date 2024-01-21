from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Town(models.Model):
    towns = models.CharField(max_length=255)

    def __str__(self):
        return self.towns

    def get_absolute_url(self):
        return reverse('home')

class Listing(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    town = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' | ' + str(self.owner)

    def get_absolute_url(self):
        return reverse('listing', args=(str(self.id)))