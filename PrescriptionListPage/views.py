from django.shortcuts import render

def prescription_list(request):
    return render(request, 'prescriptionlist.html')