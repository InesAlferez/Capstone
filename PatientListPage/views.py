from django.shortcuts import render
from .models import PatientList

def display(request):
    """patientlist"""
    
    patientlist = PatientList.objects.all()
    return render(request, 'patientlist.html', {'patientlist': patientlist})