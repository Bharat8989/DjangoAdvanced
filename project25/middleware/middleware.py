import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache  # १ तासासाठी डेटा लक्षात ठेवण्यासाठी

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"[{datetime.datetime.now()}] Request URL: {request.path}")

    def process_response(self, request, response):
        print(f"[{datetime.datetime.now()}] Response Status Code: {response.status_code}")
        return response

class BlockIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # युझरचा आयपी मिळवणे
        ip = request.META.get('REMOTE_ADDR')

        # १. तपासणे: युझर आधीच १ तासासाठी ब्लॉक आहे का?
        if cache.get(f'is_blocked_{ip}'):
            return HttpResponse("<h1>403 Forbidden: Your IP is blocked for 1 hour due to too many attempts.</h1>", status=403)

        # २. फक्त लॉगिन पेजवर (उदा. /login/ किंवा /admin/) आणि POST रिक्वेस्ट असतानाच काउंटिंग करणे
        if request.method == 'POST' and ('login' in request.path or 'admin' in request.path):
            
            # आधी किती प्रयत्न झाले ते कॅशमधून मिळवणे (नसल्यास 0)
            attempts = cache.get(f'login_attempts_{ip}', 0) + 1
            
            # ५ मिनिटांसाठी हा काउंट कॅशमध्ये सेव्ह करणे
            cache.set(f'login_attempts_{ip}', attempts, 300)
            print(f"[SECURITY] IP: {ip} ने {attempts} वा प्रयत्न केला.")

            # ३. जर ५ पेक्षा जास्त प्रयत्न झाले, तर १ तासासाठी (3600 सेकंद) ब्लॉक करणे
            if attempts >= 5:
                cache.set(f'is_blocked_{ip}', True, 3600)  # 3600 सेकंद = १ तास
                print(f"[BLOCKED] IP: {ip} ला १ तासासाठी ब्लॉक केले आहे!")
                return HttpResponse("<h1>Your IP has been blocked for 1 hour.</h1>", status=403)
