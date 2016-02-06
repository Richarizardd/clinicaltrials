from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.conf import settings

import json, sys, cgi, os

# IMPORT OUR PYTHON SCRIPTS
from stateQuery import get_recruitment_data, fill_states, get_sponsor_trials

# Create your views here.
def index(request):
	# jsonList = fill_states()
	# get_sponsor_trials()
	jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/index.html', {'datum': jsonList})


def stateAPI(request):
	if request.is_ajax():
		state = request.GET.get('state')
		data = (get_recruitment_data(state)) # get data
		html = {'data': data}

		print "AJAX call worked!"
	else:
		print "not working..."
		html = '<p>This is not ajax!</p>'

	return HttpResponse(json.dumps(html['data']))
