from django.urls import path
from .views import register , login_view , user_logout , edit_profile


urlpatterns = [
    path('register/', register, name='register'),
    path('login/' , login_view , name='login'),
    path('user_logout/' , user_logout , name='logout'),
    path('editprofile/' , edit_profile , name='editprofile')
]
