from random import choice

class RandomPoints():
	"""Класс для генерирования случайных блужданий."""

	def __init__(self, number_points = 5000):
		"""Определяет количество  случайных точек."""
		self.nmb_p = number_points
		self.x_val = [0]
		self.y_val = [0]

	def x_get_step(self):
		"""Распределение по оси Х."""
		x_direction = choice([-1, 1])
		x_distance = choice([0, 1, 3, 4, 5,7])
		self.x_step = x_direction * x_distance

	def y_get_step(self):	
	    """Распределение по оси Х."""
	    y_direction = choice([-1, 1])
	    y_distance = choice([0, 1, 3, 4, 5,7])
	    self.y_step = y_direction * y_distance

	def random_walk(self):
		"""Генерация случайных точек."""
		while len(self.x_val) < self.nmb_p:
			self.x_get_step()
			self.y_get_step()
			if self.x_step == 0 and self.y_step == 0:
				continue
			x = self.x_step + self.x_val[-1]
			y = self.y_step + self.y_val[-1]
			self.x_val.append(x)
			self.y_val.append(y)

	def show_list_walk(self):
		"""Отображение списков ходов."""
		print(self.x_val)
		print(self.y_val)


	