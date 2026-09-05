from django.http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("Shop home page")

def products(requests):
    return HttpResponse("Shop products page")