from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from deltarelations import forms
from deltarelations.models import DeltaUser

def index(request):
  template = loader.get_template('deltarelations/index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context),
  {
   'user': request.user
  })

def sign_up(request):
  if request.method == 'POST':
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
      user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password'])
      user.save()
      delta_user = DeltaUser(user = user, first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'], birthdate = form.cleaned_data['birthdate'], ethnicity = form.cleaned_data['ethnicity'], religion = form.cleaned_data['religion'], relstat = form.cleaned_data['relstat'], sex = form.cleaned_data['sex'], location = form.cleaned_data['location'])
      delta_user.save()
      return HttpResponseRedirect('/deltarelations')
  else:
    form = forms.SignUpForm()


  return render(request, 'deltarelations/sign_up.html', {'form': form})

def log_in(request): 
  if request.method == 'POST':
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username = username, password = password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/deltarelations')
  else:
    form = forms.LoginForm()

  return render(request, 'deltarelations/log_in.html', {'form': form})
  
def edit_profile(request):
  if request.method == 'POST':
    form = forms.EditProfileForm(request.POST)
    delta_user = DeltaUser(user = user, birthdate = form.cleaned_data['birthday'], ethnicity = form.cleaned_data['ethnicity'], religion = form.cleaned_data['religion'], relstat = form.cleaned_data['relstat'], sex = form.cleaned_data['sex'], location = form.cleaned_data['location'])
    delta_user.save()
    return HttpResponseRedirect('/')
  else:
    du = request.user.deltauser
    form = forms.EditProfileForm(initial={
      'first_name': du.first_name,
      'last_name': du.last_name,
      'birthdate': du.birthdate,
      'ethnicity': du.ethnicity,
      'religion': du.religion,
      'relstat': du.relstat,
      'sex': du.sex,
      'gender': du.gender,
      'location': du.location
    })
    
  return render(request, 'deltarelations/edit_profile.html',{'form':form})

def view_matches(request):
  user = request.user
  # Make sure the user is logged in before viewing this page
  if not user.is_authenticated:
    return HttpResponseRedirect('/')

  giving_advice_to = user.deltauser.provider.all()
  receiving_advice_from = user.deltauser.recipient.all()

  return render(request, 'deltarelations/view_matches.html',
  {
    'user': user,
    'giving_advice_to': giving_advice_to,
    'receiving_advice_from': receiving_advice_from
  })
