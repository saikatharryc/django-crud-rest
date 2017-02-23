from django.http import Http404
from django.shortcuts import render
from .models import Videos


def index(request):
    all_videos = Videos.objects.all()
    return render(request, 'videos/index.html', {'all_videos': all_videos})


def details(request, videos_id):
    try:
        videos = Videos.objects.get(pk=videos_id)
    except videos.DoesNotExist:
        raise Http404("videos Does Not exist")

    return render(request, 'videos/details.html', {'videos': videos})
