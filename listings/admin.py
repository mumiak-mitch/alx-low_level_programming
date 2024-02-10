from django.contrib import admin
from .models import Listing, Town, UserProfile, Comment

# Register your models here.
admin.site.register(Listing)
admin.site.register(Town)
admin.site.register(UserProfile)
admin.site.register(Comment)