from kof_api.Sword import Sword
from kof_api.Math import Math

math = Math()

class BronzeLSword(Sword):
	def __init__(self):
		self.name = "Bronze Long Sword"
		self.atk = 3.5
		self.weight = math.convert_kg_lb(1.4)
		
		super().__init__(self.name, self.atk, self.weight)