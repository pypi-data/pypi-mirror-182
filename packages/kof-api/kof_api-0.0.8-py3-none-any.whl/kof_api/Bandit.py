from kof_api.Enemy import Enemy

class Bandit(Enemy):
	def __init__(self, city, region, building):
		self.name = "Bandit"
		
		super().__init__(self.name, city, region, building)