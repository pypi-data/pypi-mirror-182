from kof_api.Sword import Sword
from kof_api.Math import Math

math = Math()

class WarmongerBarbSword(Sword):
	def __init__(self):
		self.name = "Warmonger Barbarian Sword"
		self.atk = 6.7
		self.weight = math.convert_kg_lb(1.4)
		
		super().__init__(self.name, self.atk, self.weight)