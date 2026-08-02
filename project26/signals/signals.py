from django.db.models.signals import post_save # इव्हेंट
from django.contrib.auth.models import User    # सेंडर (Sender)
from django.dispatch import receiver          # रिसीव्हर डेकोरेटर
from .models import Profile                   # रिसीव्हर मॉडेल

# @receiver डेकोरेटर सांगतो की 'post_save' आल्यावर हे फंक्शन रन करा
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # 'created' ची व्हॅल्यू True असते जर नवीन डेटा तयार झाला असेल (Update च्या वेळी False असते)
    if created:
        Profile.objects.create(user=instance)
        print(f"[SIGNAL] {instance.username} create new profile successfully.")
