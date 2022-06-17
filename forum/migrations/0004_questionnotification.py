# Generated by Django 4.0 on 2022-06-16 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_answer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_notifications', to='forum.question')),
            ],
        ),
    ]