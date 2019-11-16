from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, EmailDepartment


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductKeyForm(forms.Form):
    product_key = forms.CharField(max_length=16, widget=forms.PasswordInput())


YEARS = [x for x in range(1940, 2021)]


class ProfileEditForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    date_of_joining = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    phone_no = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_no', 'date', 'date_of_joining', 'gender', 'dept', 'cv',
                  'profile_pic']


class UsersTemp(forms.ModelForm):
    class Meta:
        model = EmailDepartment
        fields = '__all__'
