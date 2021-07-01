from django.shortcuts import get_object_or_404, render
from posts.models import *

def index(request):
    ultimos_posts = Post.objects.order_by('-publicado')[:5]
    context = {'ultimos_posts': ultimos_posts,}
    print (context)
    return render(request, 'base.html', context)

def post(request, post):
    post = get_object_or_404(Post, pk=post)
    return render(request, 'post.html', {'post': post})

def tags(request, post):
    tags = Post.objects.filter(pk=post)
    response = tags.post_set.all()
    return HttpResponse(response)

def create(request):
    return render(request, 'create_post.html')

def store(request):
    return 0
