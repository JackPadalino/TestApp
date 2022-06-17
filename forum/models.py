from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from classroom.models import Classroom
from django.utils import timezone
from django.urls import reverse

class Topic(models.Model):
    title = models.CharField(max_length=100,default=None)

    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='questions')
    title = models.CharField(max_length=100,default=None)
    content = models.CharField(max_length=500)
    project_link = models.CharField(max_length=1000,blank=True,default=None)
    image = models.ImageField(blank=True,default=None)
    video = models.CharField(max_length=1000,blank=True,default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    #date_resolved = models.DateTimeField(default=None,blank=True)

    def get_absolute_url(self):
        return reverse('question-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name} posted the question '{self.title}' - {self.date_posted}"

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    project_link = models.CharField(max_length=1000,blank=True,default=None)
    image = models.ImageField(blank=True,default=None)
    video = models.CharField(max_length=1000,blank=True,default=None)
    solution = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('answer-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        if self.solution == True:
            return f"{self.author.first_name} {self.author.last_name} answered the question '{self.question.title}' - {self.date_posted} - MARKED AS SOLUTION"
        else:
            return f"{self.author.first_name} {self.author.last_name} answered the question '{self.question.title}' - {self.date_posted}"