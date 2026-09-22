from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.student_list, name='student_list'), # Works for /students/
    path('', views.student_list, name='home'),                  # Add this line to work for /
]