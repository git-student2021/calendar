from django.shortcuts import render
from django.http import HttpResponse

from .models import Events, Time_interval

def index(request):
    events = Events.objects.all()
    intervals = Time_interval.objects.all()
    context = {
        'events': events,
        'title': 'Список событий',
        'intervals': intervals,
    }
    return render(request, 'events/index.html', context=context)