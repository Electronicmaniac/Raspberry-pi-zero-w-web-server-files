import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#print matplotlib.pyplot.get_backend()

y = [i for i in range(20, 100, 3)]
x = [i for i in range(len(y))]

plt.scatter(x,y)
plt.savefig('Graph.jpg')

#backend = matplotlib.pyplot.get_backend()
#print backend

