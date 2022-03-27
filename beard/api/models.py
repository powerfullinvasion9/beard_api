from django.db import models

class Post(models.Model):
    userId = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=160, blank=True, default='')
    body = models.TextField(blank=True, default='')

class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=160, blank=True, default='')
    email = models.EmailField(max_length=160)
    body = models.TextField(blank=True, default='')

class Album(models.Model):
    userId = models.ForeignKey('auth.User', related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=160, blank=True, default='')

class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=160, blank=True, default='')
    color = 'http://placebeard.it/640/480'
    grayScale = 'http://placebeard.it/g/640/480'

class Todo(models.Model):
    userId = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=160, blank=True, default='')
    compleated = models.BooleanField(default='False')
