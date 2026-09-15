from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') #It will go to the main template folder

def about(request):
    return render(request, 'blog/about.html') #It will go to the app's template folder which is named 'blog'