from wsgiref.util import request_uri
from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            # messages.success(request, ('Item Has Been Added To List!'))
            messages.success(request, request.POST['item']+ ' has been added to the list')
            return render(request, 'home.html', {'all_items' : all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items' : all_items})
def about(request):
    context = {'first_name': 'Evan', 'last_name' : 'Elder'}
    return render(request, 'about.html', context)