from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    publicado = models.DateTimeField('Publicado em', auto_now_add=True)
    atualizado = models.DateTimeField('Atualizado em', auto_now=True)
    
    def __str__(self):
        return self.titulo

class Tag(models.Model):
    post = models.ManyToManyField(Post)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
