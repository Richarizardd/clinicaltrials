from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
import stateQuery
import csv
import requests

open_trials = stateQuery.get_clinical_objects()
closed_trials = stateQuery.get_closed_trials()
trials = open_trials + closed_trials
counter = 0
print "Open trials: ", len(trials)
print "Closed trials: ", len(closed_trials)

def trials_to_csv():

	sponsor_scores = {}
	open_scores = {}
	closed_scores = {}
	# Scrape trials for data and write all trials to a csv file
	with open('trials.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for trial in open_trials:
			counter += 1
			print counter
			r = requests.get(trial.url)
			soup = BeautifulSoup(r.text, "html.parser")
			sponsor = soup.select("#sponsor")[0].text.strip()
			published = True
			if "No publications provided" in r.text:
				published = False		
			trial.sponsor = sponsor
			trial.published = published
			writer.writerow([trial.id, trial.sponsor, trial.published, trial.state, trial.url, trial.closed])



		
