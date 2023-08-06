from kof_api.Club import Club


class MorningStar(Club):
	def __init__(self):
		self.name = "Morningstar"
		self.atk = 3.5
		self.weight = 7.5
	
		super().__init__(self.name, self.atk, self.weight)
