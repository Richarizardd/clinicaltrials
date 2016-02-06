from django.db import models

class ClinicalTrial(models.Model):
	id = models.TextField(primary_key=True)
	sponsor = models.TextField()
	published = models.BooleanField()
	state = models.TextField()
	url = models.TextField()
	closed = models.BooleanField()
	title = models.TextField()
	condition = models.TextField()
	intervention = models.TextField()
	locations = models.TextField()
	last_changed = models.TextField()

    # def set_locations(self, x):
    #     self.locations = json.dumps(x)

    # def get_locations(self):
    #     return json.loads(self.locations)

