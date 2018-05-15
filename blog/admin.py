from django.contrib import admin

# Register your models here.
from .models import Blog  # importing the Job class created in models
admin.site.register(Blog)
