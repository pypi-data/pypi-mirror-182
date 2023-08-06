from kof_api.Animal import Animal

class Horse(Animal):
	def __init__(self):
		self.name = "Horse"
		self.can_carry = True
		self.weight = 0
		self.max_capacity = 0
		
		super().__init__(self.name, self.can_carry, self.weight, self.max_capacity)
		
		