from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template


import json, sys, cgi

# IMPORT OUR PYTHON SCRIPTS
from stateQuery import get_recruitment_data, fill_states

# Create your views here.
def index(request):
	jsonList = fill_states()

	return render(request, 'clinicalsearch/index.html', {'datum': jsonList})


def stateAPI(request):
	if request.is_ajax():
		data = (get_recruitment_data()) # get data
		html = {'data': data}

	else:
		print "not working..."
		html = '<p>This is not ajax!</p>'
	# print html
	# print "Break!"
	# print json.dumps(html)
	return HttpResponse(json.dumps(html['data']))
	# return render(request, 'clinicalsearch/index.html', {'data': data})
