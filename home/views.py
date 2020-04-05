from django.shortcuts import render
from .models import HomePage

def index(request):
    home = HomePage.objects.all().first()
    context = { 'home': home }
    return render(request, 'home/index.html', context)
    