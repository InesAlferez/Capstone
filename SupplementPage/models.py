from django.db import models

# Create your models here.
def get_supplements():
    supplements = ['Supplement 1', 'Supplement 2', 'Supplement 3', 'Supplement 4', 'Supplement 5', 'Supplement 6', 'Supplement 7', 'Supplement 8', 'Supplement 9', 'Supplement 10']
    return supplements
class Supplements(models.Model):
    name = models.CharField(max_length=200 , default='Supplement 1')
    description = models.CharField(max_length=200 , default='Description 1')
    price = models.CharField(max_length=200 , default='Price 1')
    def __str__(self):
        return self.name + ' ' + self.description + ' ' + self.price