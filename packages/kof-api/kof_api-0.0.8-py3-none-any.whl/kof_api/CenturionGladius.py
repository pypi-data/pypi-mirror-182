from kof_api.Sword import Sword
from kof_api.Math import Math

math = Math()


class CenturionGladius(Sword):
	def __init__(self):
		self.name = "Centurion Gladius"
		self.atk = 5.9
		self.weight = math.convert_kg_lb(1.3)
		
		super().__init__(self.name, self.atk, self.weight)
		