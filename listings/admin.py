from django.contrib import admin
from .models import Listing, Town

# Register your models here.
admin.site.register(Listing)
admin.site.register(Town)