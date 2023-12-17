import bleach
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Listing(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # specific = models.ForeignKey(SpecificModel, on_delete=models.CASCADE, null=True, blank=True)
    # category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    # constituencies = models.ManyToManyField(ConstituencyModel)
    # ward = models.ForeignKey(WardModel, on_delete=models.CASCADE, null=True, blank=True)
    # town = models.ForeignKey(TownModel, on_delete=models.CASCADE, null=True, blank=True)
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
    
    def clean_fields(self, exclude=None):
        # Use bleach.clean to sanitize map_url
        self.map_url = bleach.clean(self.map_url, tags=[], attributes={}, strip=True)
        return super().clean_fields(exclude=exclude)

    def get_absolute_url(self):
        return reverse('listings', args=(str(self.id)))