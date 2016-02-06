from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.conf import settings
from django.core import serializers

import json, sys, cgi, os

# IMPORT OUR PYTHON SCRIPTS
from stateQuery import fill_states, get_sponsor_trials
from clinicalsearch.models import ClinicalTrial

# Create your views here.
def index(request):
	# jsonList = fill_states()
	# get_sponsor_trials()
	# jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/index.html')

def about(request):
	# jsonList = fill_states()
	# get_sponsor_trials()
	# jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/about.html')

def contact(request):
	# jsonList = fill_states()
	# get_sponsor_trials()
	# jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/contact.html')

def map(request):
	# jsonList = fill_states()
	# get_sponsor_trials()
	jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/map.html', {'datum': jsonList})


def stateAPI(request):
	state = request.GET.get('state')
	print state
	data = ClinicalTrial.objects.filter(state=state)
	print data

	return HttpResponse(serializers.serialize('json', data), content_type="application/json")
