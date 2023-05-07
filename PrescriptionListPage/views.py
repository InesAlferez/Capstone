from django.shortcuts import render
from .models import Prescriptions
def prescription_list(request):
    """prescriptionlist"""
    
    prescription_list = Prescriptions.objects.all()
    return render(request, 'prescriptionlist.html', {'prescription_list': prescription_list})