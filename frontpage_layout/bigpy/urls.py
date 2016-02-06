from django.conf.urls import include, url
from bigpy import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
]