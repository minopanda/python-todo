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
            messages.success(request, ('Item Has Been Added To List'))
            return render(request, 'home.html', {'all_items': all_items})
            
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'first_name': 'Harry', 'last_name': 'Potter'}
    return render(request, 'about.html', context)