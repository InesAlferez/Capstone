"""
This module contains view functions for the food ordering app.
"""

from django.shortcuts import render
from .models import Fooditems

def display(request):
    """
    Display a list of food items available for order.
    """
    items = Fooditems.objects.all()
    return render(request, 'food.html', {'items': items})
