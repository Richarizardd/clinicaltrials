from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.conf import settings
from django.template.loader import get_template

from .models import Contact
from .forms import ContactForm

import json, sys, cgi, os

# IMPORT OUR PYTHON SCRIPTS
from stateQuery import get_recruitment_data, fill_states, get_sponsor_trials

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

			contact = form.save(commit=True)
			contact.contact_name = contact_name
			contact.contact_email = contact_email
			contact.contact_phone = contact_phone
			contact.content = disease_content
			contact.save()

			# # put into a template
			# template = get_template('clinicalsearch/contact_template.txt')

			# # create Context object
			# context = Context({
			# 	'contact_name': contact_name,
			# 	'contact_email': contact_email,
			# 	'contact_phone': contact_phone,
			# 	'disease_content': disease_content,
			# 	})
			# # render the Context object
			# content = template.render(context)
			# print content

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



def map(request):
	# jsonList = fill_states()
	# get_sponsor_trials()
	jsonList = {"test": "test"}
	return render(request, 'clinicalsearch/map.html', {'datum': jsonList})


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
