from django.urls import path
from .views import home_view, SignUpView

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', SignUpView.as_view(), name='signup'),
]