from django.shortcuts import render

def supplement(request):
    return render(request, 'supplement.html')