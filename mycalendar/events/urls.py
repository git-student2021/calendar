from django.urls import path

from .views import index, get_interval, view_events, add_events

urlpatterns = [
    path('', index, name='home'),
    path('interval/<int:interval_id>', get_interval, name='interval'),
    path('events/<int:events_id>', view_events, name='view_events'),
    path('events/add-events/', add_events, name='add_events'),
]