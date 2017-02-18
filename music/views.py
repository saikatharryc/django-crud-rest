from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>is it??????</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>Details For Album ID:" + str(album_id) + "</h2>")
