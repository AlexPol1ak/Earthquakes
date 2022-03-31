import matplotlib.pyplot as plt
from random_points import RandomPoints 

print("Построим 2 графикa слуайного блуждания :)")

rp1 = RandomPoints(10000)
rp2 = RandomPoints(10000)
# Запуск случайных блужданий.
rp1.random_walk()
rp2.random_walk()


plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10,9))
color1 = range(rp1.nmb_p)
color2 = range(rp2.nmb_p)

# Первое блуждание.
ax.scatter(rp1.x_val, rp1.y_val , c = color1, cmap=plt.cm.Blues, edgecolors = 'none', s =10)
ax.scatter(0, 0 , c= 'blue', edgecolors = 'none', s = 300)
ax.scatter (rp1.x_val[-1], rp1.y_val[-1], c = 'blue', edgecolors = 'none', s = 200)

# Второе блуждание.
ax.scatter(rp2.x_val, rp2.y_val , c = color2, cmap=plt.cm.Greens, edgecolors = 'none', s =10)
ax.scatter(0, 0 , c= 'green', edgecolors = 'none', s = 300)
ax.scatter (rp2.x_val[-1], rp2.y_val[-1], c = 'green', edgecolors = 'none', s = 200)

# Проверка и отображение пересечений двух блужданий.
user = input('Отобразить пересечение случайных блужданий? (Y,N)')
if user.lower() == 'y':
	intersection_x, intersection_y = [], []
	i = 0
	while i < len(rp1.x_val):
		if rp1.x_val[i] in rp2.x_val and rp1.y_val[i] in rp2.y_val:
			intersection_x.append(rp1.x_val[i])
			intersection_y.append(rp1.y_val[i])
			#print(i)
		i += 1

	if len(intersection_x) != 0:
		ax.scatter(intersection_x, intersection_y , c = 'yellow',  edgecolors = 'none', s =10, alpha=0.1)
	else:
		print("Пересечений нет")	
else:
	pass

# Отображение блужданий.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()