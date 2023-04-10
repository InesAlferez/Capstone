from django.shortcuts import render

def food(request):
    return render(request, 'food.html')
