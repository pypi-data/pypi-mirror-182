from kof_api.Merchant import Merchant

class Blacksmith(Merchant):
	def __init__(self, city, region, building):
		self.name = "Blacksmith"
		self.product_type = ["armour", "weapon", "shield"]
		self.currency_type = region.currency_type
		
		super().__init__(self.name, city, region, building)
		
	