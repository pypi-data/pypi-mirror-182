from kof_api.Animal import Animal

class Chicken(Animal):
	def __init__(self):
		self.name = "Chicken"
		self.can_carry = False
		self.weight = 20
		self.max_capacity = 0
		
		super().__init__(self.name, self.can_carry, self.weight, self.max_capacity)
		
		