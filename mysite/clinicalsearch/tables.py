from models import ClinicalTrial
from table import Table
from table.columns import Column

class ClinicalTrialTable(Table):
	id = Column(field='id')
	sponsor = Column(field='sponsor')
	url = Column(field='url')
	title = Column(field='title')
	intervention = Column(field='intervention')
	date = Column(field='last_changed')

	class Meta:
		model = ClinicalTrial


	# sponsor = models.TextField()
	# published = models.BooleanField()
	# state = models.TextField()
	# url = models.TextField()
	# closed = models.BooleanField()
	# title = models.TextField()
	# condition = models.TextField()
	# intervention = models.TextField()
	# locations = models.TextField()
	# last_changed = models.TextField()