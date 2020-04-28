from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    # .order_by('-date')[:5] Order post by date and limit to 5 blogs
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
