from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    blogs = [
        {"title": 'Python Basics', "is_featured": True, "author": 'Mayur Jadhav'},
        {"title": 'Django Basics', "is_featured": True, "author": ''},
        {"title": 'Java Basics', "is_featured": False, "author": 'Vishwas Hagare'},
    ]
    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "html_code": "<b>Welcome to my Blog</b>",
        
    }
    return render(request, 'blog/blog_details.html', context)