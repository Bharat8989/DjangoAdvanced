from . import views
from django.urls import path

urlpatterns = [
    path('api/', views.home, name='home'),
    path('api/students/', views.student, name='student')
]
