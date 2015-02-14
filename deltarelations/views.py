from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from deltarelations import forms

def index(request):
  template = loader.get_template('deltarelations/index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

def sign_up(request):
  if request.method == 'POST':
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
      user = User.objects.create_user(form.cleaned_data['username'], 
        form.cleaned_data['password'], form.cleaned_data['first_name'], form.cleaned_data['last_name'])
    user.save()
    delta_user = DeltaUser(user = user, birthdate = form.cleaned_data['birthday'], ethnicity = form.cleaned_data['ethnicity'], religion = form.cleaned_data['religion'], relstat = form.cleaned_data['relstat'], sex = form.cleaned_data['sex'], location = form.cleaned_data['location'])
    delta_user.save()
    return HttpResponseRedirect('/')
  else:
    form = forms.SignUpForm()

  return render(request, 'deltarelations/sign_up.html', {'form': form})
