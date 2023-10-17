from django.urls import path

from .views import index, get_interval

urlpatterns = [
    path('', index, name='home'),
    path('interval/<int:interval_id>', get_interval, name='interval'),
]