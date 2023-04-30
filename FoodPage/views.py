from django.shortcuts import render

def food(request):
    food = { '1': 'Food 1', '2': 'Food 2', '3': 'Food 3', '4': 'Food 4', '5': 'Food 5', '6': 'Food 6', '7': 'Food 7', '8': 'Food 8', '9': 'Food 9', '10': 'Food 10', }
    decriptions = { '1': 'Description 1', '2': 'Description 2', '3': 'Description 3', '4': 'Description 4', '5': 'Description 5', '6': 'Description 6', '7': 'Description 7', '8': 'Description 8', '9': 'Description 9', '10': 'Description 10', }
    prices = { '1': 'Price 1', '2': 'Price 2', '3': 'Price 3', '4': 'Price 4', '5': 'Price 5', '6': 'Price 6', '7': 'Price 7', '8': 'Price 8', '9': 'Price 9', '10': 'Price 10', }
    return render(request, 'food.html', {'food': food, 'descriptions': decriptions, 'prices': prices})
