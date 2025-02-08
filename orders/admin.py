from django.contrib import admin
from .models import Order, OrderedItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'order_status')
    list_filter = ('owner', 'order_status')
    search_fields = ('owner', 'id')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem)

