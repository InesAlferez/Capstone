from msilib.schema import SelfReg
from typing import Self
from django.db import models

# Create your models here.
def get_food():
    food = ['Food 1', 'Food 2', 'Food 3', 'Food 4', 'Food 5', 'Food 6', 'Food 7', 'Food 8', 'Food 9', 'Food 10']
    return food
def get_descriptions():
    descriptions = ['Description 1', 'Description 2', 'Description 3', 'Description 4', 'Description 5', 'Description 6', 'Description 7', 'Description 8', 'Description 9', 'Description 10']
    return descriptions
def get_prices():
    prices = ['Price 1', 'Price 2', 'Price 3', 'Price 4', 'Price 5', 'Price 6', 'Price 7', 'Price 8', 'Price 9', 'Price 10']
    return prices
class Food(models.Model):    
    food = models.CharField(max_length=200 , default='Food 1')
    description = models.CharField(max_length=200 , default='Description 1')    
    return Self.food + ' ' + SelfReg.descriptions + ' ' + self.prices
