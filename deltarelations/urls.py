from django.conf.urls import patterns, url

from deltarelations import views

urlpatterns = patterns('', 
  url(r'^sign_up', views.sign_up, name = 'sign_up'),
  url(r'^$', views.index, name='index')
)
