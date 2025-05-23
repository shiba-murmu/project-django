from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('noteitems/<int:id>', views.noteitems, name='noteitems'),
    
]