from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def v_index(request):
    context = {
        'products': [None, None, None, None, None,]
    }
    return render(request,'tiendapp/index.html', context)

def v_cart(request):
    context = {
        'items': [None, None, None, None, None, None,]
    }
    return render(request, 'tiendapp/cart.html', context)

def v_product_detail(request):
    #completar
    context = {}
    return render(request, 'tiendapp/product_detail.html', context)
    #el return render, enlazando el html, tiendap/product_detail.html
    #adicionar a la funcion render, contexto