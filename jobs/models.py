from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images')#image field to be uploaded by user for the job section
    summary = models.CharField(max_length=200) #summary of the job
