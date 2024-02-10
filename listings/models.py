from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

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
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #description = models.TextField()
    description = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    town = models.CharField(max_length=255)
    snippet = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name="listing_likes")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name + ' | ' + str(self.owner)

    def get_absolute_url(self):
        #return reverse('listing', args=(str(self.id)))
        return reverse('home')
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profiles/")
    website_url = models.CharField(max_length=255 ,null=True, blank=True)
    x_url = models.CharField(max_length=255 ,null=True, blank=True)
    instagram_url = models.CharField(max_length=255 ,null=True, blank=True)
    tiktok_url = models.CharField(max_length=255 ,null=True, blank=True)
    facebook_url = models.CharField(max_length=255 ,null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment_name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.listing.name, self.comment_name)