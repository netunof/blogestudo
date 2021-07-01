from posts.models import Post
from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("vá se lascar")

def post(request, post):
    return HttpResponse("You're looking at post %s." % post)

def tags(request, post):
    response = Post.objects.filter(pk=post)
    return HttpResponse(response)

