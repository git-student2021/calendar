from django.shortcuts import render
from django.http import HttpResponse

from .models import Events

def index(request):
    events = Events.objects.all()
    return render(request, 'events/index.html', {'events': events, 'title': 'Список событий'})