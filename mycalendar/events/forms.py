from django import forms
# from .models import Time_interval
from .models import Time_interval

class EventsForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название события", widget=forms.TextInput(attrs={"class": "form-control"}))
    description_event = forms.CharField(label="Описание", required=False, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 5
        }))
    need_for_notification = forms.BooleanField(label="Напомнить?", initial=True)
    interval = forms.ModelChoiceField(empty_label="Выберите время", label="Время за которое надо напомнить",
    queryset=Time_interval.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))

