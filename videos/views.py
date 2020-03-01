from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request):
    videos = Video.objects.filter(is_published = True).order_by('-pk')
    context = { 'videos': videos }
    return render(request, 'videos/index.html', context)