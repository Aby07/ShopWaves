from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index),
    path('product_list/', views.list_products, name='list_product'),
    path('product_detail/<pk>/', views.detail_product, name='detail_product'),
]