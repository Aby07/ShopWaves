from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value1, value2):
    try:
        return value1 * value2
    except (TypeError, ValueError):
        return 0  # Return 0 if multiplication fails (e.g., invalid types)
