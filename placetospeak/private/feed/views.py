from django.shortcuts import render, redirect
from .models import Post, Friend
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def home(request):
    user = request.user
    posts = Post.objects.filter(isPublic=True)
    if not user.is_anonymous:
        friends = Friend.objects.filter(creator=user).values_list('following')\
            .union(Friend.objects.filter(following=user).values_list('creator'))
        posts = posts | Post.objects.filter(author__in=friends) | Post.objects.filter(author=user)
    return render(request, 'feed/home.html', {
        'posts': posts.order_by('-id'),
        'user': user
    })


def log_in(request):
    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and len(password) >= 6:
            login(request, user)
            return JsonResponse({'result': 'ok'})
        else:
            return JsonResponse({'result': 'wrong'})
    return JsonResponse({'result': 'bad request'})


def log_out(request):
    logout(request)
    return redirect('/')
