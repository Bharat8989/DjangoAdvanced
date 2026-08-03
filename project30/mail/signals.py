from django.db.models.signals import post_save

from django.dispatch import receiver

from .models import Student

from django.core.mail import send_mail


@receiver(post_save, sender=Student)

def student_email(

    sender,

    instance,

    created,

    **kwargs

):

    if created:

        send_mail(

            "Registration",

            "Student Registered Successfully",

            "admin@gmail.com",

            [instance.email]

        )