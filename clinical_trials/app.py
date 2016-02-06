from bs4 import BeautifulSoup
from clinical_trials import Trials
import requests

url = "https://clinicaltrials.gov/show/NCT02675894"
r = requests.get(url)
soup = BeautifulSoup(r.text)
sponsor = soup.select("#sponsor")[0].text.strip()
published = True
if "No publications provided" in r.text:
	published = False
location = soup.find("td", {"headers":"locName"}).text