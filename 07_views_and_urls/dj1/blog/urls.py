from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
