from django.urls import path
from . import views

urlpatterns = [
    path('patientlist/', views.patient_list),
]