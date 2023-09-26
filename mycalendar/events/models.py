from django.utils import timezone
from django.db import models
from django.urls import reverse_lazy

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class Events(models.Model):
    REMIND_AT_CHOICES = [
        ("1", "за один час"),
        ("2", "за два часа"),
        ("4", "за четыре часа"),
        ("24", "за день"),
        ("168", "за неделю"),
    ]

    title = models.CharField(max_length=150, verbose_name="Название события")
    description_event = models.TextField(blank=True, verbose_name="Описание")
    start_of_the_event = models.DateTimeField(default=timezone.now, verbose_name="Дата начала")
    end_event = models.DateTimeField(default=one_week_hence, verbose_name="Дата завершения")
    need_for_notification = models.BooleanField(default=True, verbose_name="Напомнить")