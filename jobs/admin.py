from django.contrib import admin

# Register your models here.
from .models import Jobs #importing the Job class created in models
admin.site.register(Jobs)
