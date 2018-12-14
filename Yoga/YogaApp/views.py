from django.shortcuts import render,redirect, get_object_or_404
from .models import SignUp

# Create your views here.
def base (request):
    return render(request, 'YogaApp/base.html')

def about (request):
    return render(request, 'YogaApp/about.html')

def schedule (request):
    return render(request, 'YogaApp/schedule.html')

def community (request):
    return render(request, 'YogaApp/community.html')