from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    link_url = models.TextField(default='https://theworldofmbamg.files.wordpress.com/2012/08/mercedes-benz_cls-63-amg_by_wheelsandmore_6.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'{self.author} - {self.title}'

    def template(self):
        return f"<li>{self.author}</li>"

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    link_url = models.TextField(default='https://theworldofmbamg.files.wordpress.com/2012/08/mercedes-benz_cls-63-amg_by_wheelsandmore_6.jpg')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


    def __str__(self):
        return f'{self.author}'

