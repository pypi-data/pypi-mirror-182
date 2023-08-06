from kof_api.Item import Item


class Shield(Item):
	def __init__(self, name, defense, weight):
		self.name = name
		self.type = 'shield'
		self.equip_type = ["lhand","rhand"]
		self.atk, self.defense = (0, defense)
		
		super().__init__(self.name, self.type, self.equip_type, self.atk, self.defense, weight)