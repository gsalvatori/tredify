import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from random import *
from pylab import *


class Scatter:

	def __init__(self,dict_):
		self.fig = plt.figure(1)
		self.ax = self.fig.add_subplot(111, projection='3d')
		self.dict = dict_

	def get_colors(self):
		return cm.rainbow(np.linspace(0, 1, len(self.dict)))

	def get_shapes(self):
		return {0: 'tickleft', '|': 'vline', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', ',': 'pixel', 1: 'tickright', '+': 'plus', 'D': 'diamond', 'v': 'triangle_down',
		'1': 'tri_down', 'h': 'hexagon1', '*': 'star','<': 'triangle_left', '': 'nothing', '2': 'tri_up', 's': 'square', ' ': 'nothing',
		6: 'caretup', 'H': 'hexagon2', '3': 'tri_left', 'x': 'x', 7: 'caretdown', '4': 'tri_right', 'p': 'pentagon',
		'>': 'triangle_right', '8': 'octagon', 'o': 'circle', '.': 'point', 'd': 'thin_diamond', '^': 'triangle_up', '_': 'hline'}

	def init(self,view):

		colors = self.get_colors()
		shapes = self.get_shapes()
		marker = choice(shapes.keys())

		for i,c in zip(range(0,len(self.dict)),colors):
			xs = self.dict[i]['x']
			ys = self.dict[i]['y']
			zs = self.dict[i]['z']
			self.ax.scatter(xs, ys, zs, c=c, marker=marker)

		self.ax.set_xlabel('X Label')
		self.ax.set_ylabel('Y Label')
		self.ax.set_zlabel('Z Label')

		if view == "image":
			self.fig.savefig('scatter3D.png')
			print "Image saved on tredify folder"
		else:
			plt.show()


class Scatter2D:

	def __init__(self,dict_):
		self.fig_2d = plt.figure(2)
		self.ax_2d = self.fig_2d.add_subplot(111)
		self.dict = dict_

	def get_colors(self):
		return cm.rainbow(np.linspace(0, 1, len(self.dict)))

	def init(self,view):

		for i,c in zip(range(0,len(self.dict)),self.get_colors()):
			x = self.dict[i]['x']
			y = self.dict[i]['y']
			area = np.pi * (15 * np.random.rand(50))**2  # 0 to 15 point radiuses
			self.ax_2d.scatter(x, y, s=area, c=c, alpha=0.5)

		if view == "image":
			self.fig_2d.savefig('scatter2D.png')
			print "Image saved on tredify folder"
		else:
			plt.show()