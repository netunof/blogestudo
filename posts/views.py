from posts.forms import PostForm
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from posts.models import *

def tags(request, post):
    tags = Post.objects.filter(pk=post)
    response = tags.post_set.all()
    return HttpResponse(response)

def create(request):
    form = PostForm() # aqui validamos o formulário, ele já aponta pro model
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""ERRO""")
    else: 
        return render(request, 'forms/post_form.html')

def read(request, post=0):
    if post:
        post = get_object_or_404(Post, pk=post)
        return render(request, 'post.html', {'post': post})
    else:
        ultimos_posts = Post.objects.order_by('-publicado')
        postagens = {'ultimos_posts': ultimos_posts,}
        return render(request, 'index.html', postagens)

def update(request, post):
    post = get_object_or_404(Post, pk=post) ## funciona igual o Post.objects.get(pk = post)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'GET':
        return render(request, 'forms/post_form.html', {'post':post})
    else:
        if form.is_valid():
            form.save()
            return redirect('index')
        
def delete(request, post):
    post = get_object_or_404(Post, pk=post)
    if request.method=='POST':
        post.delete()
        return redirect('index')
