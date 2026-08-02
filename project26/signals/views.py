from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h1>Home Page</h1>")

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self,form):
        response = super().form_valid(form)
        print("[SIGNAL] User created successfully.")
        return response