from django.shortcuts import get_object_or_404, render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    high_priority_product_list = Product.objects.order_by('priority')[:4]
    latest_product_list = Product.objects.order_by('-created_at')[:8]  

    context = {
        'high_priority_product_list': high_priority_product_list,
        'latest_product_list': latest_product_list
    }

    return render(request, 'index.html', context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)

    #product_list = Product.objects.all() #fetch all product
    product_list = Product.objects.order_by('priority')
    product_paginator = Paginator(product_list, 4) #paginator used for show item in page, here 4 product are show in a single page
    product_list=product_paginator.get_page(page)

    context={
        'product': product_list
    }
    return render(request, 'products.html', context)

def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk) #fetch the product 
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
