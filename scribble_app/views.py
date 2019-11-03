from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Post
from .models import Comment

# Create your views here.
def home(request):
    return HttpResponse("Good Bye Rocket Ship! Hello new Home PandaQQ TWPRIDE <body><h1>Ni de Ming Zi</h1><div><strong>Hello</strong></div></body>")

def api_posts(request):
    all_posts = Post.objects.all()
    data = []
    for post in all_posts:
        data.append({"Author": post.author, "Title": post.title})
    return JsonResponse({"data": data, "status": 200})


def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'post_list.html', context)

def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'post_detail.html', context)

def api_comments(request):
    all_comments = Comment.objects.all()
    data = []
    for car in all_comments:
        data.append({"author": comment.author, "body": comment.body})
    return JsonResponse({"data": data, "status": 200})

def comment_list(request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, 'comment_list.html', context)