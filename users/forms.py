from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *

REGISTER_AS = [
    ('D', 'Doctor'),
    ('P', 'Patient')
]

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

class UserCreateForm(UserCreationForm):
    register_as = forms.ChoiceField(choices=REGISTER_AS, required=True, widget=forms.RadioSelect)
    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "register_as")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"

class ProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = ('name', 'phone', 'email', 'gender', 'age', 'address', 'blood_group','case_paper')


class DoctorProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = ('name', 'phone', 'email', 'gender', 'age', 'address', 'department', 'attendance', 'salary', 'status')
