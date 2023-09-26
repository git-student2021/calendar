from django.db import models




class Events(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название события")
    description_event = models.TextField(blank=True, verbose_name="Описание")
    start_of_the_event = models.DateTimeField(verbose_name="Дата начала")
    end_event = models.DateTimeField(verbose_name="Дата завершения")
    need_for_notification = models.BooleanField(default=True, verbose_name="Напомнить")