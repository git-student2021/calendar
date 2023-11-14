from django import forms
# from .models import Time_interval
from .models import Time_interval

class EventsForm(forms.Form):
    title = forms.CharField(max_length=150)
    description_event = forms.CharField()
    need_for_notification = forms.BooleanField()
    interval = forms.ModelChoiceField(queryset=Time_interval.objects.all())

