from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email, name='send_email'),      
    path('html-email/', views.html_email, name='html_email'), 
    path('template-email/', views.send_template_email, name='send_template_email'),
    path('register-student/', views.register_student, name='register_student'),
]