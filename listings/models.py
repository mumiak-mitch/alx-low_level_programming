from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name + ' | ' + str(self.owner)

    def get_absolute_url(self):
        return reverse('listing', args=(str(self.id)))