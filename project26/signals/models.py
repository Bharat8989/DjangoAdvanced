from django.db import models
from django.contrib.auth.models import User

# युझरचे अतिरिक्त प्रोफाईल मॉडेल
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
