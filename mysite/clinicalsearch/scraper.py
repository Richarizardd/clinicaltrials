from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
import stateQuery
import csv
import requests

open_trials = stateQuery.get_clinical_objects()
closed_trials = stateQuery.get_closed_trials()
trials = open_trials + closed_trials
sponsors_to_trials = {}
counter = 0
print "Open trials: ", len(trials)
print "Closed trials: ", len(closed_trials)

def trials_to_csv():
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
			if sponsor not in sponsors_to_trial:
				sponsors_to_trial[sponsor] = []
			sponsors_to_trials[sponsor].append(trial)
			writer.writerow([trial.id, trial.sponsor, trial.published, trial.state, trial.url, trial.closed])

def sponsors_impact(sponsors_ctrials_dict):
	sponsors_impact_dict = {}
	sponsors = sponsors_ctrials.keys()

	for sponsor in sponsors:
		num_completed_results = 0 
		num_completed = 0
		num_ongoing = 0

		clinicaltrials = sponsors_ctrials_dict[sponsor]
		for trial in clinicaltrials:
			if trial.published:
				num_completed_results += 1
			if trial.closed:
				num_completed += 1
			else:
				num_ongoing += 1

		sponsors_impact_dict[i] = num_completed_results/(float)num_completed

	return sponsors_impact_dict


		
