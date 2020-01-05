import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

rw = RandomWalk()
rw.fillWalk()

plt.scatter(rw.x_values,rw.y_values,s = 1)
plt.show()