from django.contrib import admin

# Register your models here.
from .models import Job #importing the Job class created in models
admin.site.register(Job) #add a Job in admin page

