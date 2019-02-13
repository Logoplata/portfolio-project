from django.contrib import admin
# Adding Blogs to admin portal
from .models import Blog 

admin.site.register(Blog)