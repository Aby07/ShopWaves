from django.db import models
from customers.models import Customer
from products.models import Product

# Order

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=(
        (LIVE,'Live'),
        (DELETE,'Delete')
    )

    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=(
        (ORDER_PROCESSED, 'ORDER_PROCESSED'),
        (ORDER_DELIVERED, 'ORDER_DELIVERED'),
        (ORDER_REJECTED, 'ORDER_REJECTED'),
    )

    order_status=models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "order-{}-{}".format(self.id,self.owner.name)

class OrderedItem(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large')
    ]

    product=models.ForeignKey(Product, related_name='added_cart', on_delete=models.SET_NULL, null=True)
    qty=models.IntegerField(default=1)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='M')
    owner=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')


