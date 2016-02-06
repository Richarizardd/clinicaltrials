############# Function to get data from clinicaltrials.gov 
# using clinical api
from clinical_trials import Trials
import json

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

# Function to return clinical trial meta data for a certain state
def get_recruitment_data():
	# create a clinical trials object for searching
	t = Trials()
	recruiting_trials = t.search(recruiting='open', count=COUNT)['search_results']['clinical_study']

	print "Success in calling get_recruitment_data!"

	return (recruiting_trials)

# Function to query number of recruiting clinical trials for each state
def fill_states():
	# create a clinical trials object for searching
	t = Trials()
	jsonList = {}
	for index in range(0, len(states_abbrev)):
		trials = t.search(recruiting='open', count=COUNT, state=states_abbrev[index])['search_results']['clinical_study']

		state = states_abbrev[index] # the state abbreviation
		numTrials = len(trials)		 # number of trials per state

		# Create the json object to be returned
		jsonList[state] = {"numTrials": numTrials}

	return jsonList
