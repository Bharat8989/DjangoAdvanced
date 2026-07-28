from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
from .forms import StudentForm 
from django.contrib import messages


def create_student(request):
    """Handles creating a new student record."""
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student created successfully.")
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'index.html', {'form': form})

def student_list(request):
    """Fetches and displays all registered students."""
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def update_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'student_list.html',
        {'form': form, 'student': student}
    )