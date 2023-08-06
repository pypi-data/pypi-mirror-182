from kof_api.Club import Club


class IronFlail(Club):
	def __init__(self):
		self.name = "Iron Flail"
		self.atk = 4
		self.weight = 6.5
		
		super().__init__(self.name, self.atk, self.weight)
