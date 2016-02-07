from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.conf import settings
from django.core import serializers
from django.template.loader import get_template
from .tables import ClinicalTrialTable

from .models import Contact
from .forms import ContactForm, SearchForm

import json, sys, cgi, os

from clinicalsearch.models import ClinicalTrial

# Create your views here.
def index(request):

	return render(request, 'clinicalsearch/index.html', {'form': SearchForm()})

def about(request):

	return render(request, 'clinicalsearch/about.html')

def problem(request):
	return render(request, 'clinicalsearch/problem.html')

def contact(request):
	form_class = ContactForm()

	# check if submit button was pushed
	if request.method == 'POST':
		form = ContactForm(request.POST)

		# check human validity 2+3=5?
		check_human = request.POST.get('human', '')

		# check using django's built in validity test
		if form.is_valid() and int(check_human) is 5:
			# get name, email and content of message
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			contact_phone = request.POST.get('contact_phone', '')
			disease_content = request.POST.get('content', '')

			# Save fields to the model
			contact = form.save(commit=True)
			contact.contact_name = contact_name
			contact.contact_email = contact_email
			contact.contact_phone = contact_phone
			contact.content = disease_content
			contact.save()

			# redirect to the contact page
			return render(request, 'clinicalsearch/contact.html', {
					'form': form_class,
					'error': 2,
				})
		else: # form is not valid
			return render(request, 'clinicalsearch/contact.html', {
				'form': form_class,
				'error': 1,
			})

	return render(request, 'clinicalsearch/contact.html', {
		'form': form_class,
		'error': 0,
	})

# works
def map(request):
	jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/map.html', {'datum': jsonList})

######################### LIST OF API CALLS ###############################
# not yet working

def searchAPI(request):
	if request.method == 'POST': # If the form has been submitted...
		form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
        	data = form.cleaned_data
        	trials = ClinicalTrial.objects.all()
        	if "disease" in data:
        		trials = trials.filter(disease=data["disease"])
        	if "sponsor" in data:
        		trials = trials.filter(sponsor=data["sponsor"])
        	if "gender" in data:
        		if data["gender"] == "Male":
        			trials = trials.filter(genders="Male")
        		if data["gender"] == "Female":
        			trials = trials.filter(genders="Female")
        	if "health" in data:
        		if data["health"] == "Must Be Ill":
        			trials = trials.filter(health=False)
        	if "min_age" in data:
        		trials = trials.filter(min_age_gte=data["min_age"])
        	if "max_age" in data:
        		trials = trials.filter(max_age_lte=data["max_age"])
        	if "state" in data:

			print form.cleaned_data['my_form_field_name']

			return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		form = ContactForm() # An unbound form


def diseaseAPI(request):
	disease = request.GET.get('disease')
	data = ClinicalTrial.objects.filter(condition=disease)

	return HttpResponse(json.dumps(data), content_type="application/json")
# works
def stateAPI(request):
	state = request.GET.get('state')
	closed = ClinicalTrial.objects.filter(state=state, ongoing=False)
	ongoing = ClinicalTrial.objects.filter(state=state, ongoing=True)
	data = {"closed": len(closed), "ongoing": len(ongoing)}
	print data
	return HttpResponse(json.dumps(data), content_type="application/json")

def completetableAPI(request):
	state = request.GET.get('state')
	completeTable = ClinicalTrialTable(ClinicalTrial.objects.filter(state=state, ongoing=False))
	return render(request, 'clinicalsearch/table.html', {"completeTable": completeTable})

def ongoingtableAPI(request):
	state = request.GET.get('state')
	ongoingTable = ClinicalTrialTable(ClinicalTrial.objects.filter(state=state, ongoing=True))
	
	print ongoingTable
	
	return render(request, 'clinicalsearch/table.html', {"ongoingTable": ongoingTable})

def minAgeAPI(request):
	min_age = request.GET.get('min_age')
	data = ClinicalTrial.objects.filter(min_age=min_age)
	print data
	print type(data)
	return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def maxAgeAPI(request):
	max_age = request.GET.get('max_age')
	data = ClinicalTrial.objects.filter(max_age=max_age)
	return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def genderAPI(request):
	genderes = request.GET.get('genders')
	data = ClinicalTrial.objects.filter(genders=genders)
	return HttpResponse(serializers.serialize('json', data), content_type="application/json")
	
def healthAPI(request):
	health = request.GET.get('health')
	data = ClinicalTrial.objects.filter(health=health)
	return HttpResponse(serializers.serialize('json', data), content_type="application/json")
