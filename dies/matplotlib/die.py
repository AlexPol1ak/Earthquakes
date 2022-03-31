from random import randint

class Die():
	"""Предстовляет модель кубика."""

	def __init__(self, sides = 6):
		"""Ининцилизирует количество  граней кубика."""
		self.num_sides = sides

	def roll(self):
		"""Осуществляет бросок кубика."""

		if self.num_sides != 0:
			self.value = randint(1, self.num_sides)
			return self.value
		else:
			return 0

	def show_sides(self):
		self.message_die = f"У кубика {self.num_sides} граней."
		print(self.message_die)

	def change_sides(self, new_num):
		"""Изменяет количество  граней кубика."""
		self.num_sides = new_num



