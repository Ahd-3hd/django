from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.http import Http404


def dynamic_lookup_view(request,id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product,id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object":obj
    }
    return render(request,'products/product_detail.html',context)

def product_delete_view(request,id):
    obj = get_object_or_404(Product,id=id)
    # obj.delete()
    if request.method == "POST":
        #confirm delete
        obj.delete()
        print('hi')
        return redirect('../../')

    context={
        "object":obj
    }
    return render(request,"products/product_delete.html",context)


def product_list_view(request):
    queryset = Product.objects.all() # will give list of all objects
    context = {
        "object_list": queryset
    }
    return render(request,'products/product_list.html',context)