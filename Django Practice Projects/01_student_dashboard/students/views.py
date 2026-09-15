from django.shortcuts import render

# Create your views here.
def profile(request):
    student = {
        "name": "Mayur Jadhav",
        "age": 22,
        "course": "Python Full Stack Development",
        "college": "ABC College",
        "email": "mayur@example.com",
        "skills": ["Python", "HTML", "CSS", "Django"],
        "is_active": True,
    }
    return render(request, "students/profile.html", {'student':student})
