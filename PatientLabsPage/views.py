from django.shortcuts import render

def patient_labs(request):
    return render(request, 'patientlabs.html')
