from django.shortcuts import render

def new_patient(request):
    return render(request, 'newpatient.html')