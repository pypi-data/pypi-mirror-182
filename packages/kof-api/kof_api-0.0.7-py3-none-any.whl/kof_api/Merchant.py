from kof_api.NPC import NPC

class Merchant(NPC):
	def __init__(self, name, city, region, building):
		self.lvl = 0
		self.health = 100
		self.has_quests = False
		self.is_merchant = True
		self.product_type = product_type
		self.products = []
		self.quests = []
		
		super().__init__(name, city, region, building)
		
		
	def setup_wares(self, wares):
		for w in wares:
			self.products.append(w)
			print(f"Added {w.name} to Merchants Sale List!")