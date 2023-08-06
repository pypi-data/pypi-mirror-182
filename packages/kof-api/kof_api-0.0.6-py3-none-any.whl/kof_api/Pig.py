from kof_api.Animal import Animal

class Pig(Animal):
	def __init__(self):
		self.name = "Pig"
		self.can_carry = False
		self.weight = 145
		self.max_capacity = 0
		
		super().__init__(self.name, self.can_carry, self.weight, self.max_capacity)