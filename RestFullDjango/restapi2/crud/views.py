from django.shortcuts import render,get_object_or_404

# Create your views here.
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer
from rest_framework import status

class DeviceListCreateView(APIView):
    """
    Handles List (GET), Create (POST), and Batch Delete (DELETE) operations.
    """
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Supports both single object and bulk/batch creation
        is_many = isinstance(request.data, list)
        serializer = DeviceSerializer(data=request.data, many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Batch Delete: Deletes multiple devices matching a list of serial numbers.
        Payload format: {"serial_nos": ["SN101", "SN102"]}
        """
        serial_nos = request.data.get('serial_nos', [])
        if not serial_nos:
            return Response({"error": "No serial numbers provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        deleted_count, _ = Device.objects.filter(serial_no__in=serial_nos).delete()
        return Response({"message": f"Successfully deleted {deleted_count} devices"}, status=status.HTTP_200_OK)


class DeviceDetailView(APIView):
    """
    Handles Single Retrieve (GET), Update (PUT/PATCH), and Delete (DELETE) using serial_no.
    """
    def get(self, request, serial_no):
        device = get_object_or_404(Device, serial_no=serial_no)
        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, serial_no):
        device = get_object_or_404(Device, serial_no=serial_no)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, serial_no):
        device = get_object_or_404(Device, serial_no=serial_no)
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, serial_no):
        device = get_object_or_404(Device, serial_no=serial_no)
        device.delete()
        return Response({"message": "Device deleted successfully"}, status=status.HTTP_204_NO_CONTENT)