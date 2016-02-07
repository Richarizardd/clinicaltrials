# Run this in the Django shell

from clinicalsearch.models import ClinicalTrial
import csv

with open('clinicalsearch/trials.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		t = ClinicalTrial(id=row[0], sponsor=row[1], published=(row[2]=="True"), state=row[3], url=row[4], closed=(row[5]=="True"), title=row[6], condition=row[7], intervention=row[8], locations=row[9], last_changed=row[10], ranking=int(row[11], min_age=int(row[12]), max_age=int(row[13]), genders=row[14], health=(row[15] == "True"))
		t.save()