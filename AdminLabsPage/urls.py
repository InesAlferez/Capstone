from django.urls import path
from . import views

urlpatterns = [
    path('adminlabs/', views.display, name='display'),
]
