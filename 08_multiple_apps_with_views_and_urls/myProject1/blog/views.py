from django.http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("Blog home page")

def about(requests):
    return HttpResponse("Blog about page")