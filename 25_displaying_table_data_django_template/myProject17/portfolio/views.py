from django.shortcuts import render
from .models import Project

# Create your views here.
def student_list(request):
    students = Project.objects.all()
    return render(request, 'portfolio/student_list.html', {'students': students})
