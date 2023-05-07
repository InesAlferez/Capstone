from django import forms
from .models import Petowners

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Petowners
        fields = ['firstname', 'lastname', 'email', 'address1', 'address2', 'city', 'state', 'zipcode', 'phonenumber', 'petid']
        labels = {'firstname': 'First Name', 'lastname': 'Last Name', 'email': 'Email', 'address1': 'Address 1', 'address2': 'Address 2', 'city': 'City', 'state': 'State', 'zipcode': 'Zip Code', 'phonenumber': 'Phone Number', 'petid': 'Pet ID',}