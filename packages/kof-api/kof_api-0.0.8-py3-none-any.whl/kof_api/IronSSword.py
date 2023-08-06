from kof_api.Sword import Sword
from kof_api.Math import Math

math = Math()

class IronSSword(Sword):
	def __init__(self):
		self.name = "Iron Short Sword"
		self.atk = 5.5
		self.weight = math.convert_kg_lb(1.4)
		
		super().__init__(self.name, self.atk, self.weight)