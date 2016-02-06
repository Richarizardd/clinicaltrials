from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),

	# Data Processing URLs
	url(r'^api/getstatedata', views.stateAPI, name='stateAPI'),
]