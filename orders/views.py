from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, OrderedItem
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages


@login_required(login_url='/account/')
def show_cart(request):
    user = request.user
    customer = user.customer_profile

    # Fetch the cart for the current customer
    cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    
    # Pass the cart object to the template
    context = {
        'cart_obj': cart_obj
    }
    return render(request, 'cart.html', context)

def remove_item_from_cart(request, pk):
    item = get_object_or_404(OrderedItem, pk=pk)
    if item:
        item.delete()
    return redirect('show_cart')

@login_required(login_url='/account/')
def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total = float(request.POST.get('total'))

            order_obj, created = Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total = total
                order_obj.save()
                status_message = "Your Order Is Proceeed."
                messages.success(request, status_message)
            else:
                status_message = "NO order available"
                messages.error(request, status_message)

        except Exception as e:
                status_message = "Error Occured"
                messages.error(request, status_message)
    return redirect('show_cart')

@login_required(login_url='/account/')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('qty', 1)) 
        size = request.POST.get('size')

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        product_obj = get_object_or_404(Product, id=product_id)
        product=Product.objects.get(pk=product_id)

        ordered_item, created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )

        if created:
            ordered_item.qty=quantity
            ordered_item.save()
        else:
            ordered_item.qty=ordered_item.qty+quantity
            ordered_item.save()

        return redirect('show_cart')
    
@login_required(login_url='/account/')
def track_order(request):
    user=request.user
    customer=user.customer_profile
    all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context = {
        'order': all_orders
        }
    return render(request, 'order.html', context)