from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Classroom,Forum,Answer,AnswerNotification

@receiver(post_save,sender=Classroom)
def create_forum(sender,instance,created,**kwargs):
    if created:
        Forum.objects.create(classroom=instance)

@receiver(post_save,sender=Answer)
def create_answer_notification(sender,instance,created,**kwargs):
    if created:
        AnswerNotification.objects.create(answer=instance,notified_user=instance.question.author)