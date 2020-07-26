from django.shortcuts import render
from .models import Blog

def blogs(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', { 'blog': blog})
