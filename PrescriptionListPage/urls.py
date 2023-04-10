from django.urls import path
from . import views

urlpatterns = [
    path('prescriptionlist/', views.prescription_list),
]
