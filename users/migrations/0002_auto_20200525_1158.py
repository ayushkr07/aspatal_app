# Generated by Django 3.0.6 on 2020-05-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='med_reps',
        ),
        migrations.AlterField(
            model_name='user',
            name='registeras',
            field=models.CharField(choices=[('D', 'Doctor'), ('P', 'Patient'), ('R', 'Receptionist')], max_length=2),
        ),
    ]
