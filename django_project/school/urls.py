from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='school-home'),
    path('about/', views.about, name='school-about'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
]
