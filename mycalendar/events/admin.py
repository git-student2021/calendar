from django.contrib import admin

from .models import Events, Time_interval

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_of_the_event', 'end_event', 'need_for_notification', 'interval')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description_event')
    list_editable = ('need_for_notification',)
    list_filter = ('need_for_notification',)

class Time_intervalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Events, EventsAdmin)
admin.site.register(Time_interval, Time_intervalAdmin)