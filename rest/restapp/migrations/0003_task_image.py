# Generated by Django 4.1.6 on 2023-04-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
