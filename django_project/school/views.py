from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required



def home(request):
    context = {
        'posts':Post.objects.all(),
    }
    return render(request, 'school/home.html', context)

def about(request):
    return render(request, 'school/about.html',{'title':'about'})

@login_required
def student(request):
    return render(request, 'school/student.html')
@login_required
def teacher(request):
    return render(request, 'school/teacher.html')
