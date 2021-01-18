import datetime
from django import template

register = template.Library()
@register.simple_tag
def current_time():
    return 'Hello I\'m a tag!!!'