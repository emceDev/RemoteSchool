from django.urls import path
from . import views
urlpatterns = [
    path('', views.classroom_template, name='classroom-classroom_template'),
    path('course_preview', views.course_preview, name='classroom-course_preview'),
    ]
