from django.db import models

# Create your models here.


class Blog(models.Model):
    # image field to be uploaded by user for the job section
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images')
    body_text = models.TextField()  # summary of the job
