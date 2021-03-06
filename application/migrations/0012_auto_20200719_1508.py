# Generated by Django 3.0.6 on 2020-07-19 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20200718_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_review',
            name='date',
            field=models.DateField(default='2020-07-19'),
        ),
        migrations.CreateModel(
            name='doctor_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.doctors')),
            ],
        ),
    ]
