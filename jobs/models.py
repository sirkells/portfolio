from django.db import models

class Jobs(models.Model):
    image = models.ImageField(upload_to='')#image field to be uploaded by user for the job section
    summary = models.CharField(max_length=200) #summary of the job
