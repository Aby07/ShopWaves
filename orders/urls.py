from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('show_cart/', views.show_cart, name='show_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<int:pk>/', views.remove_item_from_cart, name='remove_item'),
    path('checkout_cart/', views.checkout_cart, name='checkout_cart'),
]