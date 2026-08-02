from django.http import HttpResponse


def set_session_view(request):
    
    request.session['username'] = 'Navin'
    request.session['role'] = 'Admin'
    
    
    request.session.set_expiry(3600) 
    
    return HttpResponse("<h1>Session create successful!</h1><a href='/get-session/'>Click here to view data</a>")


def get_session_view(request):
    
    username = request.session.get('username', ' (Guest)')
    role = request.session.get('role', 'Not Defined')
    
    return HttpResponse(f"<h1>Session Data:</h1><p>Username: {username}</p><p>Role: {role}</p><a href='/delete-session/'>Click here to delete session</a>")


def delete_session_view(request):
    
    request.session.flush() 
    return HttpResponse("<h1>Session deleted!</h1><a href='/get-session/'>Check again</a>")


def set_cookie_view(request):
    
    response = HttpResponse("<h1>Cookie set successfully!</h1><a href='/get-cookie/'>Click here to view cookie</a>")
    response.set_cookie('username', 'Navin', max_age=3600) 
    response.set_cookie('role', 'Admin', max_age=3600) 
    
    return response 

def get_cookie_view(request):   
    
    username = request.COOKIES.get('username', ' (Guest)')
    role = request.COOKIES.get('role', 'Not Defined')
    
    return HttpResponse(f"<h1>Cookie Data:</h1><p>Username: {username}</p><p>Role: {role}</p><a href='/delete-cookie/'>Click here to delete cookie</a>")        

def delete_cookie_view(request):
    response = HttpResponse("<h1>Cookie deleted!</h1><a href='/get-cookie/'>Check again</a>")
    response.delete_cookie('username')
    response.delete_cookie('role')
    
    return response 