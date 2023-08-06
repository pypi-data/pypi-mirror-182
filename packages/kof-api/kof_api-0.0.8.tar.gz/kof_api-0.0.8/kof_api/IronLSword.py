from kof_api.Sword import Sword
from kof_api.Math import Math

math = Math()


class IronLSword(Sword):
	def __init__(self):
		self.name = "Iron Long Sword"
		self.atk = 5.5
		self.weight = math.convert_kg_lb(1)
		
		super().__init__(self.name, self.atk, self.weight)
