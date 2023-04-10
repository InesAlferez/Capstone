from django.urls import path
from . import views

urlpatterns = [
    path('patientinfo/', views.patient_info),
]