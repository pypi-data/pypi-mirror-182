from kof_api.NPC import NPC


class Enemy(NPC):
	def __init__(self, name, city, region, building):
		self.lvl = 0
		self.health = 100
		self.atk, self.defense = (0,0)
		self.has_quests = False
		self.is_merchant = False
		self.inv = {}
		
		super().__init__(name, city, region, building)
		