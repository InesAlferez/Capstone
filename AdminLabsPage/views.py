from django.shortcuts import render

def admin_labs(request):
    return render(request, 'adminlabs.html')