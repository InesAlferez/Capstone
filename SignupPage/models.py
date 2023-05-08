from django.db import models

class AuthUser(models.Model):
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    pet_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'patientaccounts'