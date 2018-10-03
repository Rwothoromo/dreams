class Bucketlist:
	name = ''
	description = ''
	items = []
	complete = False
	active = False

	def __init__(self, name, description, items, complete=False, active=False):
		self.name = name
		self.description = description
		self.items = items
		self.complete = complete
		self.active = active

	def create(self, str_p1, str_p2, list_p3):
		return None

	def index(self):
		return None

	def view(self, int_p1):
		return None

	def update(self, str_p1, str_p2, list_p3):
		return None

	def delete(int_p1):
		return None


