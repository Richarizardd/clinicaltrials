from bs4 import BeautifulSoup
from clinical_trials import Trials
from ClinicalTrial import ClinicalTrial
from clinicalsearch import models
import requests


urls = ["https://clinicaltrials.gov/ct2/show/study/NCT00456326"]
trials = []
for url in urls:
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	location = soup.find("td", {"headers":"locName"})
	if location:
		state = location.find_parent().find_previous_sibling().text
		state = state[state.index(",") + 2:]
		sponsor = soup.select("#sponsor")[0].text.strip()
		published = True
		if "No publications provided" in r.text:
			published = False		
		trial = ClinicalTrial(sponsor, published, state)

