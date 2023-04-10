from django.urls import path
from . import views

urlpatterns = [
    path('patientlabs/', views.patient_labs),
]