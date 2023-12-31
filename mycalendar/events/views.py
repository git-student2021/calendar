from django.shortcuts import render, get_object_or_404, redirect

from .models import Events, Time_interval
from .forms import EventsForm

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
    # events_item = Events.objects.get(pk=events_id)
    events_item = get_object_or_404(Events, pk=events_id)
    return render(request, 'events/view_events.html', {'events_item': events_item})

def add_events(request):
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            events = Events.objects.create(**form.cleaned_data)
            return redirect(events)
    else:
        form = EventsForm()
    return render(request, 'events/add_events.html', {'form': form})