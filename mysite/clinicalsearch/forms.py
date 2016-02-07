from django import forms
from .models import Contact

# for the contact form page linked to sendgrid
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('contact_name', 'contact_email', 'contact_phone', 'content')
	
	# init function to make it look nicer
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['contact_phone'].label = "Your phone number:"
		self.fields['content'].label = "What disease clinical trials are you interested in?"

