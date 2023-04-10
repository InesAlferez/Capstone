from django.urls import path
from . import views

urlpatterns = [
    path('patientprescription/', views.patient_prescription),
]