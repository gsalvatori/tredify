import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Scatter:

	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection='3d')
		
	def randrange(self,n, vmin, vmax):
	    return (vmax - vmin)*np.random.rand(n) + vmin

	def init(self):

		n = 100

		for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
			xs = self.randrange(n, 23, 32)
			ys = self.randrange(n, 0, 100)
			zs = self.randrange(n, zl, zh)
			self.ax.scatter(xs, ys, zs, c=c, marker=m)

		self.ax.set_xlabel('X Label')
		self.ax.set_ylabel('Y Label')
		self.ax.set_zlabel('Z Label')

		plt.show()
