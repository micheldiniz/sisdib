from django import template

register = template.Library()

@register.filter
def get_attributes(obj):

    if obj is None:
        return {}

    attrs = {}
    for attr in dir(obj):
        if not attr.startswith('_') and not callable(getattr(obj, attr)):
            attrs[attr] = getattr(obj, attr)
    return attrs
