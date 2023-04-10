from django.urls import path
from . import views

urlpatterns = [
    path('adminlabs/', views.admin_labs),
]
