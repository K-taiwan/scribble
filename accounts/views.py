from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

from scribble_app.models import Post

# Create your views here.
def register(request):
    if request.method == "POST":
        #build out data from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    #validate that passwords match
        if password == password2:
            #check if username exists in db
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'register.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error': 'Email is already taken.'}
                    return render(request, 'register.html', context)
                else:
                    #if everything is ok, create account
                    user = User.objects.create_user(
                        username=username_form, 
                        email=email_form, 
                        password=password, 
                        first_name=first_name, 
                        last_name=last_name)
                    user.save()
                    return redirect('post_list')
        else:
            context = {'error': 'Passwords do not match'}
            return render(request, 'register.html', context)
    else:
        # if not post send form
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        # authenticate user
        user = auth.authenticate(username=username_form, password=password_form)

        if user is not None:
            #login
            auth.login(request, user)
            #redirect
            return redirect('post_list')
        else:
            context = {'error': 'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('post_list')

def profile(request):
  posts = Post.objects.filter(user=request.user)
  context = {'posts':posts}
  return render(request, 'profile.html',context)