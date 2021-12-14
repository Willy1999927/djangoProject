from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth

# Create your views here.
from member.models import Character

def login(request):
    return render(request, 'DjangoProject/login.html')
def index(request):
    return render(request, 'DjangoProject/index.html')

def register_character(request):
    return render(request, 'DjangoProject/character/register_character.html')

def delete_character(request):
    return render(request, 'DjangoProject/character/delete_character.html')

def setting(request):
    return render(request, 'DjangoProject/setting.html')