from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from deltarelations import forms
from deltarelations.models import DeltaUser, Issues

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
  user = request.user
  if request.method == 'POST':
    form = forms.EditProfileForm(request.POST)
    if form.is_valid():
      delta_user = DeltaUser.objects.get(user_id = user.id)
      delta_user.first_name = form.cleaned_data['first_name']
      delta_user.last_name = form.cleaned_data['last_name']
      delta_user.birthdate = form.cleaned_data['birthdate']
      delta_user.ethnicity = form.cleaned_data['ethnicity']
      delta_user.religion = form.cleaned_data['religion']
      delta_user.relstat = form.cleaned_data['relstat']
      delta_user.sex = form.cleaned_data['sex']
      delta_user.location = form.cleaned_data['location']
      delta_user.issues_set = form.cleaned_data['issues']
      #delta_user = DeltaUser(user = user, first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'], birthdate = form.cleaned_data['birthdate'], ethnicity = form.cleaned_data['ethnicity'], religion = form.cleaned_data['religion'], relstat = form.cleaned_data['relstat'], sex = form.cleaned_data['sex'], location = form.cleaned_data['location'])
      delta_user.save()
      return HttpResponseRedirect('/deltarelations')
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
      'location': du.location,
      'issues': du.issues_set.all()
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

def find_matches(request):
  user = request.user
  # Make sure the user is logged in before viewing this page
  if not user.is_authenticated:
    return HttpResponseRedirect('/')
  delta_user = user.deltauser
  users_issues = delta_user.issues_set.all()

  # Find all the users who have the same issues as the logged in user
  relevant_users = DeltaUser.objects.filter(issues__in=users_issues).exclude(user_id = user.id).distinct()

  return render(request, 'deltarelations/find_matches.html',
  {
    'user': user,
    'relevant_users': relevant_users
  })

def add_issue(request):
  user = request.user
  if not user.is_authenticated:
    return HttpResponseRedirect('/')

  if request.method == "POST":
    form = forms.IssueForm(request.POST)
    if form.is_valid():
      issue = Issues(issue=form.cleaned_data['issue'])
      issue.save()
      return HttpResponseRedirect('/deltarelations')
  else:
    form = forms.IssueForm()

  return render(request, 'deltarelations/add_issue.html',
  {
    'form': form
  })

def log_out(request):
  logout(request)
  return HttpResponseRedirect('/deltarelations')
