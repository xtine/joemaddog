from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.models import Post


def blog(request):
    posts = Post.objects.order_by('-date_created')

    context = {'posts': posts}

    return render(request, 'blog.html', context)
