from kof_api.Item import Item

class Helmet(Item):
	def __init__(self, name, defense, weight):
		self.type = 'armour'
		self.equip_type = 'head'
		self.atk, self.defense = (0, defense)
		super().__init__(name, self.type, self.equip_type, self.atk, self.defense, weight)
	