from django.urls import path
from . import views

urlpatterns = [
    path('supplement/', views.display, name='display'),
]
