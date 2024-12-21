from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Order

def order_list(request):
    orders = Order.objects.values()
    return JsonResponse(list(orders), safe=False)
