# Run this in the Django shell

from clinicalsearch.models import ClinicalTrial
import csv

with open('trials.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		t = ClinicalTrial(id=row[0], sponsor=row[1], published=row[2], state=row[3], url=row[4])
		t.save()