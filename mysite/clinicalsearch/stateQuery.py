############# Function to get data from clinicaltrials.gov 
# using clinical api
# from django.conf.settings import STATIC_ROOT
from clinical_trials import Trials
import json, os
from ClinicalTrial import ClinicalTrial
from django.conf import settings

# list of states abbreviations and corresponding states
states_abbrev = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA',
	'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO',
	'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
	'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',
	'VA', 'WA', 'WV', 'WI', 'WY']
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
		 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
		 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
		 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
		 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
		 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
		 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

COUNT = 2 # the number of trials we want to query

# TRIALS_LIST = []

# 01: Function to query number of recruiting clinical trials for each state
def fill_states():
	# create a clinical trials object for searching
	t = Trials()
	jsonList = {} 	# json list to store number of trials/state
	trialsList = []	# list to store all 50 state's active clinical trials

	for index in range(0, len(states_abbrev)):
		trials = t.search(recruiting='open', count=COUNT, state=states_abbrev[index])['search_results']['clinical_study']

		state = states_abbrev[index] # the state abbreviation
		numTrials = len(trials)		 # number of trials per state

		# Create the json object to be returned
		jsonList[state] = {"numTrials": numTrials}

		# create a whole number of lists for passing in urls/etc.
		trialsList.append(trials) 

	TRIALS_LIST = trialsList
	print "Length of trials list: ", len(trialsList)			
			# print trial.keys()
			# keys: status, title, url, last_changed, score, condition_summary, order, nct_id

		# print len(clinical_meta_list)
		# print clinical_meta_list[0]
		# print clinical_meta_list[0].id
		# print json.dumps(trialsList[i], indent=4)

	print "Success in fill_states!"

	return jsonList

# 02: Function to return clinical trial meta data for a certain state
def get_recruitment_data(state):
	# create a clinical trials object for searching
	t = Trials()
	recruiting_trials = t.search(state=state, recruiting='open', count=COUNT)['search_results']['clinical_study']

	print "Success in calling get_recruitment_data!"

	return (recruiting_trials)

# 03: Function to help populate db with clinicaltrial objects
def get_state_trials():
	# trialsList = TRIALS_LIST
	
	# create a clinical trials object for searching
	t = Trials()
	trialsList = []	# list to store all 50 state's active clinical trials

	for index in range(0, len(states_abbrev)):
		trials = t.search(recruiting='open', count=COUNT, state=states_abbrev[index])['search_results']['clinical_study']

		# create a whole number of lists for passing in urls/etc.
		trialsList.append(trials) 

	# clinical trial object list
	clinical_meta_list = []

	# loop through list of state's trials
	for i in range(0, len(trialsList)):
		# Get the corresponding state's trials
		stateTrials = trialsList[i]

		# loop through each state's trials
		for j in range(0, len(stateTrials)):
			# create a holder for this trial
			trial = stateTrials[j]

			# Query the trial ID, and state it is in
			nct_id = trial['nct_id']
			state = states_abbrev[i]
			# sponsor = line
			url = trial['url']
			last_change = trial['last_changed']
			title = trial['title']
			condition = trial['condition_summary']
			intervention = trial['intervention_summary']

			# Create a ClinicalTrial Object to hold relevant data
			clinical_meta_data = ClinicalTrial(nct_id, None, None, state, url)
			
			# Add object to a list
			clinical_meta_list.append(clinical_meta_data)

	return clinical_meta_list

# 04: Function to return a list of trials by sponsor (restricted to USA for now)
def get_sponsor_trials():
	trialList = [] # initialize return list

	sponsorList = [] # list of sponsors from txt file

	main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
	data_file_path = os.path.join(main_dir, 'sponsors.txt')
		
	# create a clinical trials object for searching
	t = Trials()
	# file_dir = os.path.join(settings.STATIC_ROOT, 'sponsors.txt') 

	# Open local file to get list of sponsors
	with open(data_file_path, 'r') as file:
		# loop through each sponsor
		for line in file:
			trial_search = t.search(country='US', sponsor=line)
			if trial_search['search_results']['count'] > 0:
				print trial_search['search_results']['count']
				trial_results = trial_search['search_results']['clinical_study']

				# Loop through each trial for a certain sponsor
				for i in range(0, len(trial_results)):
					trial = trial_results[i]

					# Query the trial ID, and state it is in
					nct_id = trial['nct_id']
					# state = states_abbrev[i]
					sponsor = line
					url = trial['url']
					title = trial['title']
					condition = trial['condition_summary']
					intervention = trial['intervention_summary']
					last_change = trial['last_changed']

					# Create a ClinicalTrial Object to hold relevant data
					clinical_meta_data = ClinicalTrial(nct_id, None, None, state, url)
					
					# Add object to a list
					clinical_meta_list.append(clinical_meta_data)
			else:
				print trial_search['search_results']['count']

			sponsorList.append(line)





