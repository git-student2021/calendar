from django.shortcuts import render
from django.http import HttpResponse

from .models import Events

def index(request):
    events = Events.objects.all()
    res = '<h1>Список событий</h1>'
    for i in events:
        res += f'<div>\n<p>{i.title}</p>\n<p>{i.description_event}</p>\n</div>\n<hr>'
    return HttpResponse(res)

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')