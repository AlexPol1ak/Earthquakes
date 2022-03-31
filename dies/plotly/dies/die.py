from random import randint

class Die():
	"""Предстввляет кубик."""

	def __init__(self, sides = 6):
		"""Инициализирует грани кубика."""
		self.num_sides = sides

	def roll(self):
		"""Моделирует бросок кубика."""
		self.values = randint(1,self.num_sides )
		return self.values

	
