from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.conf import settings
from django.core import serializers
from django.template.loader import get_template
from .tables import ClinicalTrialTable

from .models import Contact
from .forms import ContactForm

import json, sys, cgi, os

from clinicalsearch.models import ClinicalTrial

# Create your views here.
def index(request):

	return render(request, 'clinicalsearch/index.html')

def about(request):

	return render(request, 'clinicalsearch/about.html')

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

# not yet working
def diseaseAPI(request):
	disease = request.GET.get('disease')
	data = ClinicalTrial.objects.filter(condition=disease)

	return HttpResponse(json.dumps(data), content_type="application/json")

# works
def stateAPI(request):
	state = request.GET.get('state')
	data = ClinicalTrial.objects.filter(state=state)
	print data
	return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def modalAPI(request):
	data = {test: "test"}

	return HttpResponse(serializers.serialize('json', data), content_type="application/json")
