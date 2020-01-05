import matplotlib.pyplot as plt
from RandomWalk import RandomWalk


rw = RandomWalk()
rw.fillWalk()
numPoints = list(range(rw.num_points))

plt.scatter(rw.x_values,rw.y_values,c=numPoints,cmap = plt.cm.Blues ,edgecolors='none',s = 1)
plt.show()