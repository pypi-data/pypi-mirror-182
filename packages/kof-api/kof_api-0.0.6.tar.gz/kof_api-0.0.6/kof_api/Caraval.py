from kof_api.Ship import Ship

class Caraval(Ship):
	def __init__(self):
		self.name = "Caraval"
		self.type = ["civilian", "ship"]
		self.desc = ""
		self.max_capacity = 0
		self.max_crew = 0
		
		super().__init__(self.name, self.type, self.desc, self.max_capacity, self.max_crew)