from django.urls import path
from todoapp.views import home , login , profile


urlpatterns = [
    path('home/', home, name='home'),
    path('', login, name='login'),
    path('profile/', profile, name='profile'),
]