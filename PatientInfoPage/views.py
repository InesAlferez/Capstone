from django.shortcuts import render

def patient_info(request):
    return render(request, 'patientinfo.html')