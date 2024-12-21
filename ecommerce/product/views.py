from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.values()
    return JsonResponse(list(products), safe=False)

