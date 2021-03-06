from django import forms
from django.db import models

from deltarelations.models import Issues

class SignUpForm(forms.Form):
  username = forms.CharField(label = 'Please select a username', max_length = 100)
  first_name = forms.CharField(label = 'First Name', max_length = 30)
  last_name = forms.CharField(label = 'Last Name', max_length = 30)
  password = forms.CharField(label = 'Enter your password', max_length = 100, widget = forms.PasswordInput)
  birthdate = forms.DateField(label = 'Birthday (YYYY-MM-DD)')
  ethnicity = forms.CharField(label = 'Ethnicity', max_length = 30)
  religion = forms.CharField(label = 'Religion', max_length = 30)
  relstat = forms.CharField(label = 'Relationship Status', max_length = 30)
  sex = forms.CharField(label = 'Sex', max_length = 30)
  location = forms.CharField(label = 'Location', max_length = 30)

class EditProfileForm(forms.Form):
  first_name = forms.CharField(label = 'First Name', max_length = 30)
  last_name = forms.CharField(label = 'Last Name', max_length = 30)
  birthdate = forms.DateField(label = 'Birthday (YYYY-MM-DD)', input_formats = ['%Y-%m-%d'])
  ethnicity = forms.CharField(label = 'Ethnicity', max_length = 30)
  religion = forms.CharField(label = 'Religion', max_length = 30)
  relstat = forms.CharField(label = 'Relationship Status', max_length = 30)
  sex = forms.CharField(label = 'Sex', max_length = 30)
  location = forms.CharField(label = 'Location', max_length = 30)
  issues = forms.ModelMultipleChoiceField(queryset=Issues.objects.all())

class LoginForm(forms.Form):
  username = forms.CharField(label = 'Username', max_length = 100)
  password = forms.CharField(label = 'Password', max_length = 100, widget = forms.PasswordInput)

class IssueForm(forms.Form):
  issue = forms.CharField(label = 'Issue Description', max_length = 200)
