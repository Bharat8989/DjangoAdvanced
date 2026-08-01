from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.create_student,name='create_student'),
    path('student/',views.student_list,name='student_list'),
    path('student/<int:pk>/',views.update_student,name='update_student'),
    # path('student/',views.student,name='student'),
]
 