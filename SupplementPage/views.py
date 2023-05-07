"""
This module contains view functions for the supplements ordering app.
"""

from django.shortcuts import render
from .models import Supplements

def display(request):
    """
    Display a list of food items available for order.
    """
    items = Supplements.objects.all()
    return render(request, 'supplement.html', {'items': items})