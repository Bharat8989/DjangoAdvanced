from django.apps import AppConfig


class SignalsConfig(AppConfig):
    name = 'signals'
    
    def ready(self):
        import signals.signals  # इव्हेंट्स सिग्नल्स इम्पोर्ट करा
