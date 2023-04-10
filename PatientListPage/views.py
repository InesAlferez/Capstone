from django.shortcuts import render

def patient_list(request):
    return render(request, 'patientlist.html')