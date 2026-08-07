from . import views
from django.urls import path

urlpatterns = [
    path('api/', views.home, name='home'),
    path('api/students/', views.student, name='student'),
    path('api/students/<int:id>/', views.update_student, name='update_student'),
]
 