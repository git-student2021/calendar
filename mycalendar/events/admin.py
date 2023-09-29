from django.contrib import admin

from .models import Events

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_of_the_event', 'need_for_notification')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description_event')
    list_editable = ('need_for_notification',)
    list_filter = ('need_for_notification',)

admin.site.register(Events, EventsAdmin)