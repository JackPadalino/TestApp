from collections import UserString
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from classroom.models import Classroom
from forum.models import Answer

grades = (
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12)
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    classes = models.ManyToManyField(Classroom,blank=True,default=None,related_name='profiles')
    grade = models.IntegerField(choices=grades,default=0)
    stars = models.IntegerField(default=0)
    image = models.ImageField(blank=True,default=None)

    def get_absolute_url(self):
        return reverse('profile-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
    title = models.CharField(max_length=50,default='My project')
    blurb = models.CharField(max_length=100,default='Check out my project!')
    description = models.TextField(default="I haven't written my project description yet, but trust me it will be awesome!")
    #video = models.CharField(max_length=1000,blank=True)
    #image = models.ImageField(default=None,blank=True)

    def get_absolute_url(self):
        return reverse('project-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.title}'

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('comment-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.author} commented on {self.project.user.first_name} {self.project.user.last_name}'s project"

class CommentNotification(models.Model):
    comment = models.OneToOneField(Comment,on_delete=models.CASCADE)
    notified_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_notifications')

    #def get_absolute_url(self):
    #    return reverse('comment-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.comment.author} commented on {self.comment.project.user.first_name} {self.comment.project.user.last_name}'s project."

# answer notification model
class AnswerNotification(models.Model):
    answer = models.OneToOneField(Answer,on_delete=models.CASCADE)
    notified_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answer_notifications')

    #def get_absolute_url(self):
    #    return reverse('answer-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.answer.author.first_name} {self.answer.author.last_name} responded to {self.answer.question.author.first_name} {self.answer.question.author.last_name}'s question"