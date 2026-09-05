from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("Welcome to the blog homepage!")

def about(requests):
    a = 27
    return HttpResponse(f"About page {a}.")