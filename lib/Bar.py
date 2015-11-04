from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

class Bar:

	def __init__(self,dict_):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection='3d')
		self.dict = dict_


	def get_colors(self):
		return cm.rainbow(np.linspace(0, 1, len(self.dict)))


	def init(self):

		zdir = self.dict[0]["DIRECTION"]
		colors = self.get_colors()

		for i,c in zip(range(1,len(self.dict)),colors):
			xs = self.dict[i]["xs"]
			ys = self.dict[i]["ys"]
			zs = self.dict[i]["zs"]
			self.ax.bar(xs, ys, zs=zs, zdir=zdir, color=c, alpha=0.8)

		self.ax.set_xlabel('X')
		self.ax.set_ylabel('Y')
		self.ax.set_zlabel('Z')

		plt.show()