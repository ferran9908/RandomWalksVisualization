import matplotlib.pyplot as plt
from RandomWalk import RandomWalk


rw = RandomWalk()
rw.fillWalk()
numPoints = list(range(rw.num_points))

plt.scatter(rw.x_values,rw.y_values,c=numPoints,cmap = plt.cm.Blues ,edgecolors='none',s = 1)
plt.scatter(0,0,c='green',edgecolors='none',s=10)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()