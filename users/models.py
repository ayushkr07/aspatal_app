from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

REGISTER_AS = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('R', 'Receptionist'),
    ('HR','HR')
]

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

BLOOD_GROUPS = [
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
]

class User(AbstractUser):
    registeras = models.CharField(choices=REGISTER_AS, max_length=2)

    def is_doctor(self):
        if self.registeras == 'D':
            return True
        else:
            return False

    def is_patient(self):
        if self.registeras == 'P':
            return True
        else:
            return False

    def is_receptionist(self):
        if self.registeras == 'R':
            return True
        else:
            return False

    def is_HR(self):
        if self.registeras == 'HR':
            return True
        else:
            return False

    class Meta:
        ordering = ('id',)


class UserProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)
    case_paper = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    attendance = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True, blank=True,
                              max_length=8)

    def __str__(self):
        return "{}-Profile".format(self.user)