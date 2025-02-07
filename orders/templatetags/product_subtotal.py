from django import template

register = template.Library()

@register.simple_tag(name='product_subtotal')
def product_subtotal(cart_obj):
    print('cart_objcart_obj', cart_obj.added_items.all())
    total = 0  # Initialize total to 0
    try:
        for item in cart_obj.added_items.all():  
            total += item.qty * item.product.price  # Accumulate the total
        return total
    except (TypeError, ValueError):
        return 0  # Return 0 if multiplication fails (e.g., invalid types)
