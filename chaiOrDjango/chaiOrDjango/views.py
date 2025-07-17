from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World. You are at chai or Django Home Page.")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("Hello World. You are at chai or Django About Page.")

def contact(request):
    return HttpResponse("Hello World. You are at chai or Django Contect Page.")

