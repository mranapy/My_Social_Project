import imp
from django.urls import path
from App_Login import views

app_name = "App_Login"


urlpatterns = [
    path('signup/',views.signup, name='sign_up'),
    path('login/',views.login_page, name='login'),
    path('edit/',views.edit_profile, name='edit'),
    path('logout/',views.logout_user, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('user/<username>/',views.user, name='user'),   # catch-userame
    path('follow/<username>/',views.follow, name='follow'), # catch-userame
    path('unfollow/<username>/',views.unfollow, name='unfollow'),   # catch-userame
]
