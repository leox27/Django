from django.shortcuts import render
from datetime import datetime

# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def home(request):
    context = {
        'name': 'Vishwas Vedpathak',
        'age': 22,
        'skills': ["python", "django", "reactjs"],
        'user': User('Vishwas Vedpathak', 22),
        'blog': {
            'title': "Django Template Intro",
            'content': "<b>This is Bold</b>",
            'created_at': datetime(2026, 4, 8, 12, 30, 27),
            'author': {
                'name': 'Suraj Kumar'
            }
        },
        'empty_value': None,
        'default_if_none': '',            #works when nothing is provided
    }
    return render(request, 'blog/home.html', context)