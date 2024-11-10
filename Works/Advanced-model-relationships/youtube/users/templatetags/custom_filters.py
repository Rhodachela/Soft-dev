from django import template

register = template.Library()

@register.filter
def add_suffix(value, suffix):
    return f"{value} {suffix}"
