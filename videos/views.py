from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request, vid):    
    is_detail = 'vid' in request.GET
    if is_detail:
        videos = Video.objects.filter(pk=request.GET['vid'])
    else:
        videos = Video.objects.filter(is_published = True).order_by('-pk')
    context = { 'videos': videos, 'is_detail': is_detail }
    return render(request, 'videos/index.html', context)
