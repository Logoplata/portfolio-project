from django.contrib import admin
# Adding Jobs to admin portal
from .models import Job 


admin.site.register(Job)

