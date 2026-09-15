from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    post = {
        'title': 'My second blog post',
        'description': 'django is high level python web-framework that encorages rapid development and clean, progmatic design',
        'author': 'Yes',
        'created_at': datetime(2026, 7, 23, 5, 30),
        'event_date': datetime(2027, 10, 10, 2, 39),
        'comments_count': 5,
        'price': 100,
        'number': 7,
        'tags': ['Django', 'Python', 'Web development'],
    }
    return render(request, 'blog/blog_details.html', {'post': post}) #we have to use 'post' in html file while dealing with variables