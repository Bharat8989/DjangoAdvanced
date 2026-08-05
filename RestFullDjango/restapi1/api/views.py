from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializer import StudentSerializer


# functional based api 
@api_view(['GET'])
def home(request):
    return Response({
        "message":"Welcome to DRF"
    })
    
@api_view(['GET'])
def student(request):

    # data = {
    #     "name":"Bharat",
    #     "age":22,
    #     "city":"Chandrapur"
    # }

    # return Response(data)
    
    students=Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


