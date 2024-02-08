from django.contrib import admin
from .models import Listing, Town, UserProfile

# Register your models here.
admin.site.register(Listing)
admin.site.register(Town)
admin.site.register(UserProfile)