from kof_api.Club import Club


class Bludgeon(Club):
	def __init__(self):
		self.name = "Wooden Bludgeon"
		self.atk = 2.5
		self.weight = 5
	
		super().__init__(self.name, self.atk, self.weight)
