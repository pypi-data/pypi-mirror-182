from kof_api.Merchant import Merchant

class Farmer(Merchant):
	def __init__(self, city, region, building):
		self.name = "Farmer"
		self.product_type = ["food", "animal", "plant"]
		
		super().__init__(self.name, city, region, building)