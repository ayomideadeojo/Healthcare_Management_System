# Generated by Django 3.0.8 on 2020-07-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_chats'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
