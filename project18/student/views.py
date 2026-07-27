from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Student
from .forms import StudentForm

def index(request):
    # Pass the queryset directly; Django templates handle querysets efficiently
    students = Student.objects.all()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # Instantiate an empty form for GET requests
        form = StudentForm()
        
    return render(request, 'index.html', {'students': students, 'form': form})

def student(request):
    return HttpResponse("Hello, world. You're at the student page.")
