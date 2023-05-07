from django.shortcuts import render
from .models import PetLabs

def display(request):
    """
    Display a list of food items available for order.
    """
    petlabs = PetLabs.objects.all()
    return render(request, 'adminlabs.html', {'petlabs': petlabs})