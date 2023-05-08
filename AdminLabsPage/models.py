from django.db import models

# Create your models here.
class PetLabs(models.Model):
    petlabid = models.AutoField(db_column='PetlabID', primary_key=True)  # Field name made lowercase.
    petname = models.CharField(db_column='PetName', max_length=45)  # Field name made lowercase.
    wbc = models.IntegerField(db_column='WBC')  # Field name made lowercase.
    rbc = models.IntegerField(db_column='RBC')  # Field name made lowercase.
    hgb = models.IntegerField(db_column='HGB')  # Field name made lowercase.
    differential = models.IntegerField(db_column='Differential')  # Field name made lowercase.
    statusname = models.CharField(db_column='StatusName', max_length=45)  # Field name made lowercase.
        
    class Meta:
        managed = False
        db_table = 'patientpetlabs'