from django.shortcuts import render, HttpResponseRedirect
from .models import Petowners
from .forms import NewPatientForm

def new_patient(request):
    if request.method != 'POST':
        form = NewPatientForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/PatientHomePage/patienthome/')
    else:
        form = NewPatientForm()
    return render(request, 'newpatient.html', {'form': form})