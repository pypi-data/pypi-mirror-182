from kof_api.Item import Item

class Sword(Item):
	def __init__(self, name, atk, weight):
		self.type = 'weapon'
		self.equip_type = ['rhand', 'lhand']
		self.defense = 0
		
		super().__init__(name, self.type, atk, self.defense, weight)