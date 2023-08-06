from kof_api.Sword import Sword
from kof_api.Math import Math

math = Math()

class BronzeSSword(Sword):
	def __init__(self):
		self.name = "Bronze Short Sword"
		self.atk = 3
		self.weight = math.convert_kg_lb(.6)
		
		super().__init__(self.name, self.atk, self.weight)
	