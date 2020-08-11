
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow, world. You're at the blog index.")
# Create your views here.
