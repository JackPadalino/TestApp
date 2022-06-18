from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# school year model
class SchoolYear(models.Model):
    year = models.IntegerField(default=1900)

    def get_absolute_url(self):
        return reverse('school_year-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.year}'

# classroom model
class Classroom(models.Model):
    title = models.CharField(max_length=50,default='My Classroom')
    school_year = models.ForeignKey(SchoolYear,on_delete=models.CASCADE,related_name='classrooms')
    join_code = models.CharField(max_length=10,default='abc123')
    
    def get_absolute_url(self):
        return reverse('classroom-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.title} - {self.school_year}'

# forum model
class Forum(models.Model):
    classroom = models.OneToOneField(Classroom,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('forum-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.classroom}'

# topic model
class Topic(models.Model):
    title = models.CharField(max_length=100,default=None)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='topics')

    def get_absolute_url(self):
        return reverse('topic-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.title}'

# question model
class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='questions')
    title = models.CharField(max_length=100,default=None)
    content = models.CharField(max_length=500)
    project_link = models.CharField(max_length=1000,blank=True,default=None)
    image = models.ImageField(blank=True,default=None)
    video = models.CharField(max_length=1000,blank=True,default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='questions')

    def get_absolute_url(self):
        return reverse('question-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name} posted the question '{self.title}' - {self.date_posted}"

# answer model
class Answer(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    content = models.CharField(max_length=500)
    project_link = models.CharField(max_length=1000,blank=True,default=None)
    image = models.ImageField(blank=True,default=None)
    video = models.CharField(max_length=1000,blank=True,default=None)
    solution = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='answers')

    def get_absolute_url(self):
        return reverse('answer-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        if self.solution == True:
            return f"{self.author.first_name} {self.author.last_name} answered the question '{self.question.title}' - {self.date_posted} - MARKED AS SOLUTION"
        else:
            return f"{self.author.first_name} {self.author.last_name} answered the question '{self.question.title}' - {self.date_posted}"

# answer notification model
class AnswerNotification(models.Model):
    answer = models.OneToOneField(Answer,on_delete=models.CASCADE)
    notified_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answer_notifications')

    #def get_absolute_url(self):
    #    return reverse('answer-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.answer.author.first_name} {self.answer.author.last_name} responded to {self.answer.question.author.first_name} {self.answer.question.author.last_name}'s question"