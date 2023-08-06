from kof_api.Ship import Ship


class WarGalleon(Ship):
	def __init__(self):
		self.name = "War Galleon"
		self.type = ["military", "ship"]
		self.desc = ""
		self.max_capacity = 0
		self.max_crew = 0
		
		super().__init__(self.name, self.type, self.desc, self.max_capacity, self.max_crew)