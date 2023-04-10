from django.urls import path
from . import views

urlpatterns = [
    path('supplement/', views.supplement),
]
