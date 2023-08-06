from kof_api.Merchant import Merchant

class Alchemist(Merchant):
	def __init__(self, city, region, building):
		self.name = "Alchemist"
		self.product_type = ['potion', 'plant']
		
		super().__init(self.name, city, region, building)