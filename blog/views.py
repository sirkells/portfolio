from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def allblogs(request):
    blog_list = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blog_list':blog_list})

def detail(request, blog_id): #function for giving each blog post an id so you can search based on id
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'detailblog': detailblog})
    
