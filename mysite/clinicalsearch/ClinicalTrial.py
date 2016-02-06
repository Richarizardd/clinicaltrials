class ClinicalTrial:
	"""Object Clinical Trial"""

	def __init__(self, ID, sponsor, published, state, url, closed, title, condition, intervention, last_changed):
		self.id = ID 
		self.sponsor = sponsor
		self.published = published
		self.state = state
		self.url = url
		self.closed = closed
		self.title = title
		self.condition = condition
		self.last_changed = last_changed
		self.intervention = intervention

# temp = ["Mayo", "BGH", "JHU", "JHU", "BGH", "Mayo", "Mayo", "BGH"]
# trials = [ClinicalTrial(sponsor) for sponsor in temp]

# sponsors = {};
# for trial in trials:
# 	if trial.sponsor not in sponsors:
# 		sponsors[trial.sponsor] = []
# 	sponsors[trial.sponsor].append(trial)