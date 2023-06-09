# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=45)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20)  # Field name made lowercase.
    employeeroleid = models.IntegerField(db_column='EmployeeRoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class Employeetype(models.Model):
    employeeroleid = models.AutoField(db_column='EmployeeRoleID', primary_key=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employeetype'


class Fooditems(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fooditems'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    petownerid = models.IntegerField(db_column='PetOwnerID')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.
    shippingdate = models.DateField(db_column='ShippingDate')  # Field name made lowercase.
    trackingnumber = models.CharField(db_column='TrackingNumber', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Patientaccounts(models.Model):
    accountid = models.AutoField(db_column='accountID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    pet_name = models.CharField(max_length=150)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'patientaccounts'


class Petlabs(models.Model):
    petlabid = models.AutoField(db_column='PetlabID', primary_key=True)  # Field name made lowercase.
    petid = models.IntegerField(db_column='PetID')  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID')  # Field name made lowercase.
    wbc = models.IntegerField(db_column='WBC')  # Field name made lowercase.
    rbc = models.IntegerField(db_column='RBC')  # Field name made lowercase.
    hgb = models.IntegerField(db_column='HGB')  # Field name made lowercase.
    differential = models.IntegerField(db_column='Differential')  # Field name made lowercase.
    statusid = models.IntegerField(db_column='StatusID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'petlabs'


class Petlabstatus(models.Model):
    statusid = models.AutoField(db_column='StatusID', primary_key=True)  # Field name made lowercase.
    statusname = models.CharField(db_column='StatusName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'petlabstatus'


class Petowners(models.Model):
    petownerid = models.AutoField(db_column='PetOwnerID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=45)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20)  # Field name made lowercase.
    petid = models.IntegerField(db_column='PetID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'petowners'


class Pets(models.Model):
    petid = models.AutoField(db_column='PetID', primary_key=True)  # Field name made lowercase.
    petfirstname = models.CharField(db_column='PetFirstName', max_length=45)  # Field name made lowercase.
    petlastname = models.CharField(db_column='PetLastName', max_length=45)  # Field name made lowercase.
    petownerid = models.IntegerField(db_column='PetOwnerID', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    breed = models.CharField(db_column='Breed', max_length=45)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pets'


class Petvisits(models.Model):
    petvisitid = models.AutoField(db_column='PetVisitID', primary_key=True)  # Field name made lowercase.
    petid = models.IntegerField(db_column='PetID')  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID')  # Field name made lowercase.
    visitnotes = models.CharField(db_column='VisitNotes', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'petvisits'


class Prescriptions(models.Model):
    prescriptionid = models.AutoField(db_column='PrescriptionID', primary_key=True)  # Field name made lowercase.
    prescriptionname = models.CharField(db_column='PrescriptionName', max_length=45)  # Field name made lowercase.
    petid = models.IntegerField(db_column='PetID')  # Field name made lowercase.
    petownerid = models.IntegerField(db_column='PetOwnerID')  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID')  # Field name made lowercase.
    prescriptionstatusid = models.IntegerField(db_column='PrescriptionStatusID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescriptions'


class Prescriptionstatus(models.Model):
    prescriptionstatusid = models.AutoField(db_column='PrescriptionStatusID', primary_key=True)  # Field name made lowercase.
    prescriptionstatus = models.CharField(db_column='PrescriptionStatus', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescriptionstatus'


class Supplements(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplements'


class Useraccounts(models.Model):
    accountid = models.AutoField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'useraccounts'


class Userroles(models.Model):
    userroleid = models.AutoField(db_column='UserRoleID', primary_key=True)  # Field name made lowercase.
    userrole = models.CharField(db_column='UserRole', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userroles'
