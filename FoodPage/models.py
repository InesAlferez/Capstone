from django.db import models

class Fooditems(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=13, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'fooditems'
        