# Generated by Django 4.1.5 on 2023-12-21 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_exercise_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='title',
        ),
    ]