from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from App_Login.forms import CreateNewUser,LoginForm, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from App_Login.models import UserProfile,Follow
from django.contrib.auth.decorators import login_required
from App_Posts.forms import PostForm


######### Registration #########
def signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_login/signup.html',context={'title':'Sign Up Instragram','form':form})


######### Login #########
def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Posts:home'))

    return render(request, 'App_Login/login.html', context={'title':'Login','form':form})


######### Edit Profile #########
@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/profile.html', context={'form':form, 'title':'Edit Profile . Social'})

######### Logout #########
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

######### Profile #########
@login_required
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/user.html', context={'title':'User','form':form})

######### Other User Profile #########
@login_required
def user(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_Login:profile'))
    context = {
        'user_other':user_other,
        'already_followed':already_followed
    }
    return render(request, 'App_Login/user_other.html', context)

######### Follow User #########
@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_Login:user', kwargs={'username':username}))

######### Unfollow User #########
@login_required
def unfollow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_Login:user', kwargs={'username':username}))
