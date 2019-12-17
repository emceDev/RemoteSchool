from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'school/home.html')

def about(request):
    return render(request, 'school/about.html',{'title':'about'})
