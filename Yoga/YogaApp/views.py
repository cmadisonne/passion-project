from django.shortcuts import render,redirect, get_object_or_404
from .forms import RequestForm, ContactForm, EventForm
from .models import Events
from django.db.models import Q

# Create your views here.
def base (request):
    return render(request, 'YogaApp/base.html')

def about (request):
    return render(request, 'YogaApp/about.html')

def schedule (request):
    return render(request, 'YogaApp/schedule.html')

def community (request):
    q = request.GET.get('query', None)
    if q:
        result = Events.objects.filter(Q(description__icontains=q) | Q(name__icontains=q))
    else:
        result = Events.objects.none()
    events = Events.objects.all()
    return render(request, 'YogaApp/community.html', {'events': events, 'q':q, 'result':result})

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'YogaApp/contact.html', {'form':form})

def request (request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request')
    else:
        form = RequestForm()
        return render(request, 'YogaApp/request.html', {'form':form})