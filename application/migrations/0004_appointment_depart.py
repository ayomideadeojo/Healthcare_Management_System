# Generated by Django 3.0.8 on 2020-07-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20200713_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='depart',
            field=models.CharField(default='Neurology', max_length=50),
            preserve_default=False,
        ),
    ]
