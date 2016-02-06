class ClinicalTrial:
	"""Object Clinical Trial"""

	def __init__(self, ID, sponsor, published, state, url, closed, title, condition, intervention, locations, last_changed):
		self.id = ID 
		self.sponsor = sponsor
		self.published = published
		self.state = state
		self.url = url
		self.closed = closed
		self.title = title
		self.condition = condition
		self.intervention = intervention
		self.locations = locations
		self.last_changed = last_changed