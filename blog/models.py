from django.db import models

# Create your models here.


class Blog(models.Model):
    # image field to be uploaded by user for the job section
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images')
    body_text = models.TextField()  # summary of the job

    def __str__(self):#func that displays the title as header in admin page
        return self.title

    def summary(self): #function to summarise the body_text so it displays olnly the first 100 chr
        return self.body_text[:100]

    def date_format(self): #fumction to format the date to only date without time
        return self.date.strftime('%b %e %Y')