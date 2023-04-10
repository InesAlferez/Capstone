from django.shortcuts import render

def pharmacy(request):
    return render(request, 'pharmacy.html')