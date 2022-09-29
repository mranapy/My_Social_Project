from django.urls import path
from App_Posts import views

app_name = "App_Posts"

urlpatterns = [
    path('',views.home, name='home'),
    path('liked/<pk>/',views.liked, name='liked'),  # catch- pk
    path('unliked/<pk>/',views.unliked, name='unliked'),    # catch- pk
]