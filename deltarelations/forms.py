from django import forms
from django.db import models

class SignUpForm(forms.Form):
  username = forms.CharField(label = 'Please select a username', max_length = 100)
  first_name = forms.CharField(label = 'First Name', max_length = 30)
  last_name = forms.CharField(label = 'Last Name', max_length = 30)
  password = forms.CharField(label = 'Enter your password', max_length = 100, widget = forms.PasswordInput)
  birthdate = forms.DateField(label = 'Birthday (YYYY-MM-DD)', input_formats = '%Y-%m-%d')
  ethinicity = forms.CharField(label = 'Ethnicity', max_length = 30)
  religion = forms.CharField(label = 'Religion', max_length = 30)
  relstat = forms.CharField(label = 'Relationship Status', max_length = 30)
  sex = forms.CharField(label = 'Sex', max_length = 30)
  location = models.CharField(max_length = 30)

class EditProfileForm(forms.Form):
  first_name = forms.CharField(label = 'First Name', max_length = 30)
  last_name = forms.CharField(label = 'Last Name', max_length = 30)
  birthdate = forms.DateField(label = 'Birthday (YYYY-MM-DD)', input_formats = '%Y-%m-%d')
  ethinicity = forms.CharField(label = 'Ethnicity', max_length = 30)
  religion = forms.CharField(label = 'Religion', max_length = 30)
  relstat = forms.CharField(label = 'Relationship Status', max_length = 30)
  sex = forms.CharField(label = 'Sex', max_length = 30)
  location = models.CharField(max_length = 30)
