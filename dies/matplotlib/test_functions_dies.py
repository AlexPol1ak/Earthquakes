import unittest
from die import Die
from functions_dies import boundary_values_dies as bvd

class TestFunctionDies(unittest.TestCase):
	"""Тесты для 'functions_dies.py'."""

	def setUp(self):
		"""Создает модели трех кубиков."""
		self.die1 = Die()
		self.die2 = Die()
		self.die3 = Die(8)
		self.die4 = Die(10)
		self.dies = [self.die1, self.die2, self.die3, self.die4]

	def test_boundary_values_dies(self):
		"""Проверяет правильно ли возвращаются суммы минимальных и максимальных значений 
		всех брошеных кубиков"""
		valuemin = bvd('min', self.dies)
		valuemax = bvd('max', self.dies )
		self.assertEqual(valuemin, 4)
		self.assertEqual(valuemax, 30)

if __name__ == '__main__':
	unittest.main()
