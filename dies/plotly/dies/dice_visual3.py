from plotly.graph_objs import Bar ,Layout
from plotly import offline
from die import Die

die_1 = Die(6)
die_2 = Die(6)
throw = []
for v in range(50000):
	val = die_1.roll() * die_2.roll()
	throw.append(val)

analysis = []
max_rts = die_1.num_sides + die_2.num_sides 
for val_e in range(3, max_rts+1):
	ans =  throw.count(val_e)
	analysis.append(ans)
print(max_rts)

x_val = list(range(1, max_rts +1))
data = [Bar(x=x_val, y=analysis )]
x_axis_cnfg = {"title": "Result", 'dtick': 1}
y_axis_cnfg = {'title': 'Frequency'}
my_layout = Layout(title='Result of rolling two D6 D6 (multiplication) 50000 items', xaxis=x_axis_cnfg, yaxis=y_axis_cnfg)
offline.plot({'data': data, 'layout': my_layout}, filename='D6_D6_D6.html')

