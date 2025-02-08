from django import template

register = template.Library()

@register.simple_tag(name='order_status')
def order_status(status):
    status_array = ['', 'confirmed', 'processed', 'delivered', 'rejected']
    return status_array[status]
