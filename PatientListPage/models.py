from django.db import models

# Create your models here.
class PatientList(models.Model):
    ownerid = models.IntegerField(db_column='OwnerID', primary_key=True)  # Field name made lowercase.
    petowner = models.CharField(db_column='PetOwner', max_length=100)  # Field name made lowercase.
    petname = models.CharField(db_column='PetName', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=45)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=45)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'petownerpets'