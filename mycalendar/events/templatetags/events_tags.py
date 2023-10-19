from django import template

from events.models import Time_interval

register = template.Library()

@register.simple_tag()
def get_time_interval():
    return Time_interval.objects.all()