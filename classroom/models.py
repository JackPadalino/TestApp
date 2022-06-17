from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    title = models.CharField(max_length=50,default='My Classroom')
    year = models.IntegerField(default=1900)
    join_code = models.CharField(max_length=10,default='abc123')

    def __str__(self):
        return f'{self.title} | {self.year}'