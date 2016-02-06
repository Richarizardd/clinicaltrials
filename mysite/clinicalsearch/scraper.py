from bs4 import BeautifulSoup
from ClinicalTrial import ClinicalTrial
import stateQuery
import csv
import requests

# open_trials = stateQuery.get_state_trials()
# closed_trials = stateQuery.get_closed_trials()
# trials = open_trials + closed_trials
# print "Open trials: ", len(open_trials)
# print "Closed trials: ", len(closed_trials)

# Calculate sponsor rankings and write them to a csv file
def sponsors_impact(sponsors_ctrials):
	sponsors_impact = {}
	max_ongoing = 0
	sponsors_ongoing = {}	# A map from sponser name to the number of ongoing trials
	for sponsor in sponsors_ctrials:
		num_completed_results = 0 
		num_completed = 0
		num_ongoing = 0

		clinicaltrials = sponsors_ctrials[sponsor]
		for trial in clinicaltrials:
			if trial.closed:
				num_completed += 1
				if trial.published:
					num_completed_results += 1
			else:
				num_ongoing += 1

		if num_ongoing > max_ongoing:
			max_ongoing = num_ongoing

		sponsors_ongoing[sponsor] = num_ongoing
		if num_completed != 0:
			sponsors_impact[sponsor] = num_completed_results/float(num_completed)

	print sponsors_impact
	with open('rankings.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for sponsor in sponsors_impact:
			sponsors_impact[sponsor] += sponsors_ongoing[sponsor] / float(max_ongoing)
			writer.writerow([sponsor, sponsors_impact[sponsor]])

def test_sponsors_impact():
	sponsor_to_trials = {}
	with open('trials.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			trial = ClinicalTrial(ID=row[0], sponsor=row[1], published=(row[2] == "True"), state=row[3], url=row[4], closed=(row[5] == "True"), title=row[6], condition=row[7], intervention=row[8], locations=row[9], last_changed=row[10])
			if trial.sponsor not in sponsor_to_trials:
				sponsor_to_trials[trial.sponsor] = []
			sponsor_to_trials[trial.sponsor].append(trial)
	sponsors_impact(sponsor_to_trials)

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
			try: 
				writer.writerow([trial.id, trial.sponsor, trial.published, trial.state, trial.url, trial.closed, trial.title, trial.condition, trial.intervention.encode('ascii', 'ignore'), trial.locations, trial.last_changed])
				if sponsor not in sponsor_to_trials:
					sponsor_to_trials[sponsor] = []
				sponsor_to_trials[sponsor].append(trial)
			except UnicodeEncodeError as ude:
				print "unicode err"
				continue


#trials_to_csv(trials)
test_sponsors_impact()


		
