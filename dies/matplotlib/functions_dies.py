def boundary_values_dies(boundary_values,listdies):
	"""Принимает списко экземпляров класса 'Die.py'.
	Возвращает минимальную либо максимальную сумму броска всех кубиков."""
	minsum = 0
	maxsum = 0
	try:
		for ld in listdies:
			minsum += (ld.num_sides - ld.num_sides)+1
			maxsum += ld.num_sides
	except:
		print("Функция принимает только список экземпляров класса 'Die.py'")
	else:
		if boundary_values.lower() == 'min':
			return minsum
		elif boundary_values.lower() == 'max':
			return maxsum
		else:
			print("Не удалось вычислить значения")






















	# 	if boundary_values == 'min':
	# 	min_values = []
	# 	for die in dies:
	# 		values = []
	# 		for i in range(1001):
	# 			val = die.roll()
	# 			values.append(val)
	# 		v = min(values)
	# 		min_values.append(v)
	# 	min_value = sum(min_values)
	# 	return min_value
	# elif boundary_values == 'max':
	# 	max_values = []
	# 	for die in dies:
	# 		values = []
	# 		for i in range(1001):
	# 			val = die.roll()
	# 			values.append(val)
	# 		v = max(values)
	# 		max_values.append(v)
	# 	max_value = sum(max_values)
	# 	return max_value