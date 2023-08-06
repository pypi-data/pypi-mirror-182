from kof_api.Enemy import Enemy

class Thief(Enemy):
	def __init__(self, city, region, building):
		self.name = "Thief"
		
		super().__init__(self.name, city, region, building)