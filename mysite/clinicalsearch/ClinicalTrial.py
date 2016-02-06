class ClinicalTrial:
	"""Object Clinical Trial"""

	def __init__(self, ID, sponsor, published, state, url, closed):
		self.id = ID 
		self.sponsor = sponsor
		self.published = published
		self.state = state
		self.url = url
		self.closed = closed

# temp = ["Mayo", "BGH", "JHU", "JHU", "BGH", "Mayo", "Mayo", "BGH"]
# trials = [ClinicalTrial(sponsor) for sponsor in temp]

# sponsors = {};
# for trial in trials:
# 	if trial.sponsor not in sponsors:
# 		sponsors[trial.sponsor] = []
# 	sponsors[trial.sponsor].append(trial)