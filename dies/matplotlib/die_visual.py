from matplotlib import pyplot as plt
from die import Die
from functions_dies import boundary_values_dies as bvd

# Создание двух шестигранных кубиков
my_die1 = Die(6)
my_die2 = Die(6)
my_die3 = Die(6)
my_die4 = Die(6)
my_die5 = Die(6)
my_die6 = Die(6)
dies = [my_die1,my_die2,my_die3,my_die4,my_die5,my_die6]

# Выполняем 5000 бросков двух шестигранных кубиков
values = []
for i in range(10000):
	v = my_die1.roll() + my_die2.roll() + my_die3.roll()+ my_die4.roll() +my_die5.roll() + my_die6.roll() 
	values.append(v)
# Подсчет выпавших значений
num_val = []
for i in range(bvd('min',dies), bvd('max',dies )):
	num = values.count(i)
	num_val.append(num)

# Строим гисторграмму
# x = values
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10,7))
ax.set_title("Cтатистика бросков шести  кубиков D6", fontsize=16)
ax.set_xlabel("Результат броска", fontsize=14)
ax.set_ylabel("Количество выпадаймых значений", fontsize=14)
ax.tick_params(axis='both', labelsize=12)
ax.hist(values, bins=50,histtype='bar', color='red')
ax.axis([0, bvd('max', dies), 0, max(num_val)+50])
plt.show()
#plt.savefig('D6x6_10000roll.png')
print(num_val)



