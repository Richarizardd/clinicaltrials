from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
import stateQuery
import csv
import requests

trials = stateQuery.get_clinical_objects()
print trials
for trial in trials:
	r = requests.get(trial.url)
	soup = BeautifulSoup(r.text, "html.parser")
	location = soup.find("td", {"headers":"locName"})
	if location:
		state = location.find_parent().find_previous_sibling().text
		state = state[state.index(",") + 2:]
		sponsor = soup.select("#sponsor")[0].text.strip()
		published = True
		if "No publications provided" in r.text:
			published = False		
		trial.state = state
		trial.sponsor = sponsor
		trial.published = published

with open('trials.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	for trial in trials:
		writer.writerow([trial.id, trial.sponsor, trial.published, trial.state])

