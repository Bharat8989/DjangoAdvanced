from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Student
# send html email format
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

def send_email(request):

    send_mail(

        subject="Welcome",

        message="Welcome to Django Email Tutorial",

        from_email=settings.DEFAULT_FROM_EMAIL,

        recipient_list=[
            "kadamb208@gmail.com"
        ],

        fail_silently=False

    )

    return HttpResponse(
        "Email Sent"
    )
    
    
def html_email(request):

    subject = "Welcome"

    from_email = "bk2905190@gmail.com"

    to = ["kartikpchavhan2004@gmail.com"]

    html_content = """

    <h1>Welcome</h1>

    <p>This is HTML Email</p>

    """

    email = EmailMultiAlternatives(

        subject,

        "",

        from_email,

        to

    )

    email.attach_alternative(

        html_content,

        "text/html"

    )

    email.send()

    return HttpResponse("HTML Email Sent")


# dynamic email sending 

def send_template_email(request):
    
    html = render_to_string(
        "emails/welcome_email.html",
        {
            "username": "Kartik"
        }
    )

    
    email = EmailMultiAlternatives(
        subject="Welcome",
        body="Welcome to our platform!",  # टेक्स्ट बॅकअप (पर्यायी)
        from_email="bk2905190@gmail.com",
        to=["kartikpchavhan2004@gmail.com"]
    )
    

    email.attach_alternative(html, "text/html")
    
  
    email.send()

    return HttpResponse("Template Email Sent")


def register_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # मॉडेलमध्ये डेटा सेव्ह होताच सिग्नल आपोआप मेल पाठवेल
        Student.objects.create(name=name, email=email) 
        # return redirect('success_url')
        
    return render(request, 'register.html')