class ClinicalTrial:
	"""Object Clinical Trial"""

	def __init__(self, sponsor):
		self.sponsor = sponsor

	def getSponsor(self):
		return self.sponsor


temp = ["Mayo", "BGH", "JHU", "JHU", "BGH", "Mayo", "Mayo", "BGH"]
search_results = [ClinicalTrial(sponsor) for sponsor in temp]



sponors = {};
for clinicaltrial in search_results:
	currSponsor = clinicaltrial.getSponsor()
	if currSponsor in sponsors.keys():
		sponsors[currSponsor].append(clinicaltrial)
	else:
		sponsors[currSponsor] = [clinicaltrial]