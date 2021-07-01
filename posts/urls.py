from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post>', views.post, name='post'),
    path('posts/create', views.create, name='create'),
    path('posts/store', views.store, name='store'),
    path('posts/<int:post>/tag', views.tags, name='tag'),
]