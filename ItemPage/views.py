from django.shortcuts import render

def item(request):
    return render(request, 'item.html')