from django.shortcuts import render,redirect, get_object_or_404
from .forms import EventForm,ContactForm

# Create your views here.
def base (request):
    return render(request, 'YogaApp/base.html')

def about (request):
    return render(request, 'YogaApp/about.html')

def schedule (request):
    return render(request, 'YogaApp/schedule.html')

def community (request):
    return render(request, 'YogaApp/community.html')

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'YogaApp/contact.html', {'form':form})