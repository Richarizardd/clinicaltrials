# Run this in the Django shell

from clinicalsearch.models import ClinicalTrial
import csv

with open('trials.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		t = ClinicalTrial(id=row[0], sponsor=row[1], published=row[2], state=row[3], url=row[4], closed=row[5], title=row[6], condition=row[7], last_changed=row[8], intervention=row[9])
		t.save()