import bleach
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    categories = models.CharField(max_length=255)

    def __str__(self):
        return self.categories
    
class Sub_County(models.Model):
    subCounties = models.CharField(max_length=255)

    def __str__(self):
        return self.subCounties
    
class Ward(models.Model):
    wards = models.CharField(max_length=255)

    def __str__(self):
        return self.wards
    
class Town(models.Model):
    towns = models.CharField(max_length=255)

    def __str__(self):
        return self.towns
    

class Listing(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)

    category = models.CharField(max_length=255, default="Organization")
    sub_county = models.CharField(max_length=255, default="Hamisi")
    ward = models.CharField(max_length=255, default="Kaimosi")
    town = models.CharField(max_length=255, default="Cheptulu")

    description = models.TextField()
    web_url = models.URLField(null=True, blank=True)
    hours = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    social_media = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    
    # Update map_url field to use bleach.clean for sanitization
    map_url = models.URLField(max_length=255, null=True, blank=True)

    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    other_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + '|' + str(self.author)
    
    def save(self, *args, **kwargs):
        # Use bleach.clean to sanitize the map_url field before saving
        if self.map_url:
            self.map_url = bleach.clean(self.map_url)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('listings', args=(str(self.id)))