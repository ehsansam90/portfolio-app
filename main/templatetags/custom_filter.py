# main/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """ Custom filter to get dictionary item by key """
    return dictionary.get(key, 0)
