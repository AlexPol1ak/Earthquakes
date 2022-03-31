import unittest
from die import Die

class TestDie(unittest.TestCase):
	"""Тесты для класса Die"""

	def setUp(self):
		"""Создает модель кубика."""
		self.my_die1 = Die()
		self.my_die2 = Die(8)

	def test_add_defult_die(self):
		"""Проверяет количество граней по умолчанию."""
		self.assertEqual(self.my_die1.num_sides, 6)

	def test_add_die(self):
		"""Проверяет количество заданных граней."""
		self.assertEqual(self.my_die2.num_sides, 8)

	def test_roll_default(self):
		"""Проверяет максимальные и минимальные значение, 
		которые выдает кубик c гранями  по умолчанию, при броске."""
		self.values1 = []
		for i in range(5000):
			self.value1 = self.my_die1.roll()
			self.values1.append(self.value1)
		self.assertEqual(min(self.values1), 1)
		self.assertEqual(max(self.values1), 6)

	def test_roll(self):
		"""Проверяет максимальные и минимальные значения,
		 которые выдает кубик c заданными грянями ,при броске."""
		self.values2 = []
		for i in range(1000):
			self.value2 = self.my_die2.roll()
			self.values2.append(self.value2)
		self.assertEqual(min(self.values2), 1)
		self.assertEqual(max(self.values2), 8)

	def test_change_sides(self):
		"""Проверяет изминение граней кубика."""
		self.my_die1.change_sides(10)
		self.assertEqual(self.my_die1.num_sides, 10)

	def test_show_sides(self):
		"""Проверяет вывод количества граней кубика."""
		self.my_die1.show_sides()
		self.assertEqual(self.my_die1.message_die, f"У кубика {self.my_die1.num_sides} граней.")




if __name__ == '__main__':
	unittest.main()


