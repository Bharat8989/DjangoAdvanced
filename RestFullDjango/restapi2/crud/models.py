from django.db import models

class Device(models.Model):
    serial_no = models.CharField(max_length=100, unique=True)
    model_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.serial_no} - {self.model_name}"
