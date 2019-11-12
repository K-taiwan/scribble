from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    return HttpResponse("Good Bye Rocket Ship! Hello new Home PandaQQ TWPRIDE <body><h1>Ni de Ming Zi</h1><div><strong>Hello</strong></div></body>")

#################################    Posts   ##############################################

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

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = post.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    context = {'form': form, 'header': "Add New Post"}
    return render(request, 'post_form.html', context)

@login_required
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'header': f"Edit {post.author}"}
    return render(request, 'post_form.html', context)

@login_required
def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')

#################################    Comments   ##############################################



def comment_list(request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, 'comment_list.html', context)

@login_required
def comment_create(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    context = {'form': form, 'header': f"Add Comment for {post.author}"}
    return render(request, 'comment_form.html', context)

@login_required
def comment_edit(request, pk, comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form, 'header': f"Edit {comment.author}"}
    return render(request, 'comment_form.html', context)

@login_required
def comment_delete(request, pk, comment_pk):
    Comment.objects.get(id=comment_pk).delete()
    return redirect('post_detail', pk=pk)

