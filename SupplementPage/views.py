from django.shortcuts import render
from .models import Supplements


def supplement(request):
    supplements = {
        "1": "Supplement 1",
        "2": "Supplement 2",
        "3": "Supplement 3",
        "4": "Supplement 4",
        "5": "Supplement 5",
        "6": "Supplement 6",
        "7": "Supplement 7",
        "8": "Supplement 8",
        "9": "Supplement 9",
        "10": "Supplement 10",
    }
    descriptions = {
        "1": "Description 1",
        "2": "Description 2",
        "3": "Description 3",
        "4": "Description 4",
        "5": "Description 5",
        "6": "Description 6",
        "7": "Description 7",
        "8": "Description 8",
        "9": "Description 9",
        "10": "Description 10",
    }
    prices = {
        "1": "Price 1",
        "2": "Price 2",
        "3": "Price 3",
        "4": "Price 4",
        "5": "Price 5",
        "6": "Price 6",
        "7": "Price 7",
        "8": "Price 8",
        "9": "Price 9",
        "10": "Price 10",
    }
    return render(
        request,
        "supplement.html",
        {"supplements": supplements, "descriptions": descriptions, "prices": prices},
    )
