from kof_api.Club import Club

class IronMace(Club):
	def __init__(self):
		self.name = "Iron Mace"
		self.atk, self.defense = (3.2, 0)
		self.weight = 7
	
		super().__init__(self.name, self.type, self.atk, self.defense, self.weight)