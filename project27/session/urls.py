from django.urls import path
from .views import delete_cookie_view, get_cookie_view, set_session_view, get_session_view, delete_session_view,set_cookie_view

urlpatterns = [
    path('set-session/', set_session_view, name='set_session'),
    path('get-session/', get_session_view, name='get_session'),
    path('delete-session/', delete_session_view, name='delete_session'),
    
     path('set-cookie/', set_cookie_view, name='set_cookie'),
    path('get-cookie/', get_cookie_view, name='get_cookie'),
    path('delete-cookie/', delete_cookie_view, name='delete_cookie'),
]
