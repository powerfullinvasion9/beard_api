from django.contrib.auth.models import User
from api.models import Post, Comment, Album, Photo, Todo
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['userId', 'id', 'title', 'body']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['postId', 'id', 'name', 'email', 'body']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['userId', 'id', 'title']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['albumId', 'id', 'title', 'color', 'grayScale']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['userId', 'id', 'title', 'compleated']
