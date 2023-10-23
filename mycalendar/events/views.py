from django.shortcuts import render
from django.http import HttpResponse

from .models import Events, Time_interval

def index(request):
    events = Events.objects.all()
    context = {
        'events': events,
        'title': 'Список событий',
    }
    return render(request, 'events/index.html', context=context)

def get_interval(request, interval_id):
    events = Events.objects.filter(interval_id=interval_id)
    interval = Time_interval.objects.get(pk=interval_id)
    return render(request, 'events/interval.html', {'events': events, 'interval': interval})

def view_events(request, events_id):
    events_item = Events.objects.get(pk=events_id)
    return render(request, 'events/view_events.html', {'events_item': events_item})