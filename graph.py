import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


y = [i for i in range(20, 100, 3)]
x = [i for i in range(len(y))]

plt.scatter(x,y)
plt.savefig('Graph.jpg')
