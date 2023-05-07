from django.urls import path
from . import views

urlpatterns = [
    path('newpatient/', views.new_patient, name='form'),
]