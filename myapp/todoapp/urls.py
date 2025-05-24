from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('noteitems/<int:id>', views.noteitems, name='noteitems'),
    path('delete_note/<int:id>', views.delete_note, name='delete_note'),
]