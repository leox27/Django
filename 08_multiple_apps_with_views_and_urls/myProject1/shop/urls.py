from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('products/', views.products, name='shop-products'),
]
