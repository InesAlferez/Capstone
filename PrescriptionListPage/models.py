from django.db import models

# Create your models here.
class Prescriptions(models.Model):
    prescriptionid = models.AutoField(db_column='PrescriptionID', primary_key=True)  # Field name made lowercase.
    prescriptionname = models.CharField(db_column='PrescriptionName', max_length=45)  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=91)  # Field name made lowercase.
    petname = models.CharField(db_column='PetName', max_length=45)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescriptionlist'
