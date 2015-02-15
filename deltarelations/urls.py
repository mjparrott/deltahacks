from django.conf.urls import patterns, url

from deltarelations import views

urlpatterns = patterns('', 
  url(r'^sign_up', views.sign_up, name = 'sign_up'),
  url(r'^log_in', views.log_in, name = 'log_in'),
  url(r'^view_matches', views.view_matches, name = 'view_matches'),
  url(r'^$', views.index, name='index')
)
