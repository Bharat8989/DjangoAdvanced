from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Student

def student_list(request):

    students = Student.objects.all()

    paginator = Paginator(students, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'student_list.html',
        {'page_obj': page_obj}
    )