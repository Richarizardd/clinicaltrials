from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^problem', views.problem, name='problem'),
	url(r'^map', views.map, name='map'),
	url(r'^contact', views.contact, name='contact'),

	# Data Processing URLs
	url(r'^api/getstatedata', views.stateAPI, name='stateAPI'),
	url(r'^api/getdiseasedata', views.diseaseAPI, name='diseaseAPI'),
	# url(r'^api/getmodal)
]