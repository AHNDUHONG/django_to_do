from wsgiref.util import request_uri
from django.shortcuts import render
from .models import List

# Create your views here.
def home(request):
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items' : all_items})

def about(request):
    context = {'first_name': 'Evan', 'last_name' : 'Elder'}
    return render(request, 'about.html', context)