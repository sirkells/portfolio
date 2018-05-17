from django.shortcuts import render
from .models import Blog
# Create your views here.


def allblogs(request):
    blog_list = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blog_list':blog_list})
