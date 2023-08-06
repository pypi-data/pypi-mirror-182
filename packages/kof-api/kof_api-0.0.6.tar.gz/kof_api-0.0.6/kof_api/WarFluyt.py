from kof_api.Ship import Ship

class WarFluyt(Ship):
	def __init__(self):
		self.name = "War Fluyt"
		self.type = ["military", "ship"]
		self.desc = ""
		self.max_cap = 0
		self.max_crew = 0
		
		super().__init__(self.name, self.type, self.desc, self.max_cap, self.max_crew)
		