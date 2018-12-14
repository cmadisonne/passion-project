from django.shortcuts import render,redirect, get_object_or_404
from .models import SignUp

# Create your views here.
def base (request):
    return render(request, 'YogaApp/base.html')