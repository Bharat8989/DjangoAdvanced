from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        # fields = ['id', 'serial_no', 'model_name', 'manufacturer', 'created_at']
        fields='__all__'
