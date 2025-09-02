from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'website/index.html')

def contact(request):
    return HttpResponse("Working Fine contact")

def about(request):
    return HttpResponse("Working Fine about")
