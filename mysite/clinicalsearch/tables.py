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