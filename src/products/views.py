from django.shortcuts import render
from .models import Product


def dynamic_lookup_view(request,id):
    obj = Product.objects.get(id=id)
    print(obj)
    context = {
        "object":obj
    }
    return render(request,'products/product_detail.html',context)