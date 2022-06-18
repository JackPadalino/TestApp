from django.contrib import admin
from .models import SchoolYear,Classroom,Forum,Topic,Question,Answer,AnswerNotification

admin.site.register(SchoolYear)
admin.site.register(Classroom)
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerNotification)