from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
import csv
import requests

urls = ["https://clinicaltrials.gov/ct2/show/study/NCT00456326"]
trials = []
for url in urls:
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	location = soup.find("td", {"headers":"locName"})
	if location:
		state = location.find_parent().find_previous_sibling().text
		state = state[state.index(",") + 2:]
		sponsor = soup.select("#sponsor")[0].text.strip()
		published = True
		if "No publications provided" in r.text:
			published = False		
		trial = ClinicalTrial(id, sponsor, published, state)
		print trial.sponsor, trial.published, trial.state

with open('trials.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	for trial in trials:
		writer.writerow([trial.id, trial.sponsor, trial.published, trial.state])

