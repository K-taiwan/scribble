from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ('author', 'title', 'body', 'link_url')

class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = ('author', 'body', 'link_url')