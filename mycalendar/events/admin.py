from django.contrib import admin

from .models import Events

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_of_the_event', 'need_for_notification')

admin.site.register(Events, EventsAdmin)