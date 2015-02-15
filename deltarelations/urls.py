from django.conf.urls import patterns, url

from deltarelations import views

urlpatterns = patterns('', 
  url(r'^sign_up', views.sign_up, name = 'sign_up'),
  url(r'^log_in', views.log_in, name = 'log_in'),
  url(r'^edit_profile', views.edit_profile, name = 'edit_profile'),
  url(r'^view_matches', views.view_matches, name = 'view_matches'),
  url(r'^find_matches', views.find_matches, name = 'find_matches'),
  url(r'^add_issue', views.add_issue, name = 'add_issue'),
  url(r'^log_out', views.log_out, name = 'log_out'),
  url(r'^$', views.index, name='index')
)
