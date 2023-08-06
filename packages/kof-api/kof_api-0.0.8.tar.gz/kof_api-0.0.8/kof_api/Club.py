from kof_api.Item import Item


class Club(Item):
	def __int__(self, name, atk, weight):
		self.type = 'weapon'
		self.equip_type = ['rhand', 'lhand']
		self.defense = 0
		
		super().__init__(name, self.type, self.equip_type, atk, self.defense, weight)
