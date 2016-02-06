from django.shortcuts import render
from django.http import HttpResponse

# Main page
def index(request):
	return render(request, 'layout/index.html')

# The about page, with website description and useful links
def about(request):
	return render(request, 'layout/about.html')	