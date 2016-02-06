from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
import requests

states = set(["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",])
urls = ["https://clinicaltrials.gov/ct2/show/study/NCT00456326"]
trials = []
for url in urls:
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	location = soup.find("td", {"headers":"locName"})
	if location:
		state = location.find_parent().find_previous_sibling().text
		state = state[state.index(",") + 2:]
		if state in states:
			sponsor = soup.select("#sponsor")[0].text.strip()
			published = True
			if "No publications provided" in r.text:
				published = False		
			trial = ClinicalTrial(sponsor, published, state)

