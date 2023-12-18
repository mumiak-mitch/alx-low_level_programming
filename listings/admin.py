from django.contrib import admin
from .models import Listing, Category, Sub_County, Ward, Town

# Register your models here.
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Sub_County)
admin.site.register(Ward)
admin.site.register(Town)