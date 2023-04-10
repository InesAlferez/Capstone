from django.shortcuts import render

def patient_prescription(request):
    return render(request, 'patientprescription.html')