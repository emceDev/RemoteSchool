from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def classroom_template(request):
    return render(request, 'classroom/classroom_template.html')
@login_required
def course_preview(request):
    return render(request, 'classroom/course_preview.html')

@login_required
def student(request):
    return render(request, 'classroom/student.html')
@login_required
def teacher(request):
    return render(request, 'classroom/teacher.html')
