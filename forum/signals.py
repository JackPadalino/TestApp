from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Question,Answer#,AnswerNotification

# this function will generate a profile when a new user is created
#@receiver(post_save,sender=Answer)
#def create_answer_notification(sender,instance,created,**kwargs):
#    if created:
#        AnswerNotification.objects.create(answer=instance)

#@receiver(post_save,sender=User)
#def save_profile(sender,instance,**kwargs):
#    instance.profile.save()