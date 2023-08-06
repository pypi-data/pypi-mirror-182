from kof_api.Merchant import Merchant

class StableMaster(Merchant):
	def __inti__(self, city, region, building):
		self.name = "Stable Master"
		self.product_type = ["animal"]
		
		super().__init__(self.name, city, region, building)