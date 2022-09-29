from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from App_Login.models import Follow
from django.contrib.auth.models import User
from App_Posts.models import Post,Like


########## Post, Follow, Search, Liked All View Home ##########
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    # print(liked_post_list)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    if request.method == "GET":
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
        posts = Post.objects.all()
        context={
            'title':'Home',
            'search':search,
            'result':result,
            'posts':posts,
            'liked_post_list':liked_post_list
            }
    return render(request,'App_Posts/home.html', context)

######### Post Liked #########
@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

######### Post Unliked #########
@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))