from django.shortcuts import render

from .models import Expo

def index(request):
    context = { 
        'expos': Expo.objects.filter(expo_publish=True).order_by('-expo_startdate'),
    }   
    return render(request, 'expo/index.html', context)
    