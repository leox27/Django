from . import views
from django.urls import path, re_path

urlpatterns = [

    # path() → Used to capture parameters directly from the URL.
    # <int:post_id> means the URL must contain an integer.
    # Example: /post/10/ → post_id = 10
    path('post/<int:post_id>/', views.post_details, name='post_details'),

    # <str:username> → Captures a string from the URL.
    # Example: /user/mayur/ → username = "mayur"
    path('user/<str:username>/', views.user_profile, name='user_profile'),

    # Multiple URL parameters can be captured.
    # Example: /article/2026/08/
    # year = 2026, month = 08
    path('article/<int:year>/<int:month>/<int:days>/', views.article_details, name='article_details'),

    # re_path() → Used when URL parameters need a Regular Expression.
    # [0-9]{4} → Exactly 4 digits.
    # (?P<year>...) → Stores the matched value in 'year'.
    # Example: /article/2026/ → year = 2026
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_details, name='article_by_year'),
]
