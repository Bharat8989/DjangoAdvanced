from django.shortcuts import render 
from django.http import HttpResponse,JsonResponse
from .models import Student

# Create your views here.

def index(request):
    student = list(Student.objects.all().values())
    
    print(student)
    return JsonResponse(student,safe=False)
    # student_names = ", ".join([s.name for s in student])
    
    
    # if not student_names:
    #     return HttpResponse("Hello, ALL student. ")
        
    # return HttpResponse(f"Hello, ALL student: {student_names}")
   

def student(request):
    return HttpResponse("Hello, world. You're at the student page.")