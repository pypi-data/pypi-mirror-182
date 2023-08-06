from kof_api.Animal import Animal

class Cow(Animal):
	def __init__(self):
		self.name = "Cow"
		self.can_carry = True
		self.weight = 300
		self.max_capacity = 300
		
		super().__init__(self.name, self.can_carry, self.weight, self.max_capacity)