import matplotlib.pyplot as plt
from random_points import RandomPoints 

print("Построим график слуайного блуждания :)")

rp = RandomPoints(20000)
rp.random_walk()
plt.style.use('classic')
fig, ax = plt.subplots(dpi=128)
color = range(rp.nmb_p)
ax.scatter(rp.x_val, rp.y_val , c = color, cmap=plt.cm.Blues, edgecolors = 'none', s =5)
ax.scatter(0, 0 , c= 'green', edgecolors = 'none', s = 100)
ax.scatter (rp.x_val[-1], rp.y_val[-1], c = 'red', edgecolors = 'none', s = 100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()