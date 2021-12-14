from django.urls import path
from member.views import *

from django.contrib.auth import views as auth_views

from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('setting/',views.setting, name='setting'),
    path('register/',views.register_character, name='register'),
    path('delete/',views.delete_character, name='delete'),

]