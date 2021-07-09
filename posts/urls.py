from django.urls import path

from . import views

urlpatterns = [
    path('', views.read, name='index'),
    path('posts/<int:post>', views.read, name='post'),
    path('posts/create', views.create, name='create'),
    path('posts/<int:post>/update', views.update, name='update'),
    path('posts/<int:post>/delete', views.delete, name='delete'),
    path('posts/<int:post>/tag', views.tags, name='tag'),
]