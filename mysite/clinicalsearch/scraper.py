from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
import stateQuery
import csv
import requests

open_trials = stateQuery.get_state_trials()
closed_trials = stateQuery.get_closed_trials()
trials = open_trials + closed_trials
print "Open trials: ", len(open_trials)
print "Closed trials: ", len(closed_trials)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Scrape trials for data and write all trials to a csv file
def trials_to_csv(trials):
	counter = 0
	sponsor_to_trials = {}
	with open('trials.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for trial in trials:
			counter += 1
			print counter
			r = requests.get(trial.url)
			soup = BeautifulSoup(r.text, "html.parser")
			sponsor = soup.select("#sponsor")[0].text.strip()
			published = True
			if "No publications provided" in r.text:
				published = False
			locations = [location.text for location in soup.findAll("td", {"headers":"locName"})]	
			trial.sponsor = sponsor
			trial.published = published
			trial.locations = locations
			if sponsor not in sponsor_to_trials:
				sponsor_to_trials[sponsor] = []
			sponsor_to_trials[sponsor].append(trial)
			# print "Id: ", is_ascii(trial.id)
			# print "Sponsor: ", is_ascii(trial.sponsor)
			# print "State: ", is_ascii(trial.state)
			# print "URL: ", is_ascii(trial.url)
			# print "Condition: ", is_ascii(trial.condition)
			# print "Drug: ", is_ascii(trial.intervention)
			try: 
				writer.writerow([trial.id, trial.sponsor, trial.published, trial.state, trial.url, trial.closed, trial.title, trial.condition, trial.intervention.encode('ascii', 'ignore'), trial.locations, trial.last_changed])
			except UnicodeEncodeError as ude:
				print "unicode err"
				continue

def sponsors_impact(sponsors_ctrials_dict):
	sponsors_impact_dict = {}
	sponsors = sponsors_ctrials.keys()

	for sponsor in sponsors:
		num_completed_results = 0 
		num_completed = 0
		num_ongoing = 0

		clinicaltrials = sponsors_ctrials_dict[sponsor]
		for trial in clinicaltrials:
			if trial.closed:
				num_completed += 1
				if trial.published:
					num_completed_results += 1
			else:
				num_ongoing += 1

		sponsors_impact_dict[i] = num_completed_results/float(num_completed)

	return sponsors_impact_dict

trials_to_csv(trials)



		
