from django.urls import path

from .views import index, get_interval

urlpatterns = [
    path('', index),
    path('interval/<int:interval_id>', get_interval),
]