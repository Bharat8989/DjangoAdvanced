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
    
@api_view(['GET', 'POST'])
def student(request):

    # data = {
    #     "name":"Bharat",
    #     "age":22,
    #     "city":"Chandrapur"
    # }

    # return Response(data)
    
    if request.method=='GET':
        
    
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    elif request.method=='POST':
        # this is main line for deserialization, it will take the data from request and convert it into python object and validate it
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# update by id  this method is put 

@api_view(['PUT'])
def update_student(request, id): # 'id' इथल्या नावाशी मॅच होतो
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Student Updated Successfully",
            "data": serializer.data  # अपडेट झालेला डेटा पाहण्यासाठी हा चांगला पर्याय आहे
        })

    return Response(serializer.errors, status=400) # एरर असेल तर ४०० स्टेटस कोड द्या
