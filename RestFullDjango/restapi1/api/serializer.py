from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # serializer/Deserializer will use the Student model to serialize data and deserialize data
        fields = '__all__'
        # fields=['name','age','city']
