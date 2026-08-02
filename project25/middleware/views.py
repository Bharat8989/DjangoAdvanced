from django.http import HttpResponse

# मुख्य होम पेज व्ह्यू (तुमचा मूळ कोड)
def home_view(request):
    return HttpResponse("Welcome to the Home Page! <br><a href='/login/'>लॉगिन करण्यासाठी इथे क्लिक करा</a>")

# टेस्टिंगसाठी साधा लॉगिन व्ह्यू
def test_login_view(request):
    # जर युझरने फॉर्म सबमिट केला (POST Request पाठवली)
    if request.method == 'POST':
        # इथे आपण मुद्दाम नेहमी 'चुकीचा पासवर्ड' असा रिस्पॉन्स देऊ जेणेकरून मिडलवेअर काउंट करेल
        return HttpResponse("Invalid Username or Password! <br><a href='/login/'>पुन्हा प्रयत्न करा</a>")
    
    # साधं लॉगिन फॉर्म दाखवण्यासाठी HTML रेंडर करणे
    html_form = """
    <h2>🔒 Login Page (Testing Rate Limit)</h2>
    <form method="POST" action="/login/">
        <!-- टेस्टिंगसाठी CSRF टोकन नसला तरी चालेल, किंवा मिडलवेअरमध्ये सूट दिली असेल -->
        <input type="text" placeholder="Username" name="user"><br><br>
        <input type="password" placeholder="Password" name="pass"><br><br>
        <button type="submit">Login</button>
    </form>
    """
    return HttpResponse(html_form)
