# Generated by Django 4.0 on 2022-06-16 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_delete_answernotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='author',
        ),
    ]