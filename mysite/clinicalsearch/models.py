from django.db import models

class ClinicalTrial(models.Model):
	id = models.TextField(primary_key=True)
	sponsor = models.TextField()
	published = models.BooleanField()
	state = models.TextField()
	url = models.TextField()
	closed = models.BooleanField()
	title = models.TextField()
	last_changed = models.TextField()
	intervention = models.TextField()
