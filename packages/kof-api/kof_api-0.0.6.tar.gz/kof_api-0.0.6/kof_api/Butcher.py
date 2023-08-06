from kof_api.Merchant import Merchant

class Butcher(Merchant):
	def __init__(self, city, region, building):
		self.name = "Butcher"
		self.product_type = ["meat"]
		
		super().__init__(self.name, city, region, building)