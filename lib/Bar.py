from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from pylab import *
from random import *


class Bar:

	def __init__(self,dict_):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection='3d')
		self.dict = dict_

	def get_colors(self):
		return cm.rainbow(np.linspace(0, 1, len(self.dict)))

	def z_coordinates(self):
		z_coordinates = []
		for i in range(1,len(self.dict)):
			z_coordinates.append(self.dict[i]["zs"])
		return z_coordinates

	def init(self,view):

		zdir = self.dict[0]["DIRECTION"]
		colors = self.get_colors()

		for i,c,z in zip(range(1,len(self.dict)),colors,self.z_coordinates()):
			xs = self.dict[i]["xs"]
			ys = self.dict[i]["ys"]
			self.ax.bar(xs, ys, zs=z, zdir=zdir, color=c, alpha=0.8)

		self.ax.set_xlabel('X')
		self.ax.set_ylabel('Y')
		self.ax.set_zlabel('Z')

		if view == "Image":
			savefig('bar3D.png')
			print "Image saved on tredify folder"
		else:
			plt.show()


class Bar2D:

	def __init__(self,dict_):
		self.fig_2d = plt.figure()
		self.ax_2d = self.fig_2d.add_subplot(111)
		self.dict = dict_

	def get_colors(self):
		return cm.rainbow(np.linspace(0, 1, len(self.dict)))

	def init(self,view):

		colors = self.get_colors()

		x_cs = self.dict[1]['xs']
		y_cs = self.dict[1]['ys']      
		N = len(x_cs)
		ind = np.arange(N)  
		plt.bar(ind, x_cs, y_cs, color=choice(colors))

		if view == "Image":
			savefig('bar2D.png')
			print "Image saved on tredify folder"
		else:
			plt.show()

