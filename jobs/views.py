from django.shortcuts import render

# Create your views here.

from .models import Job

def home(request):
    job_list = Job.objects
    return render(request, 'jobs/home.html', {'job_list': job_list}) #job_lisst is put in a dict form so that we can call it from the html