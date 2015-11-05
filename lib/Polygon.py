from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
import matplotlib.pyplot as plt
import numpy as np
from pylab import *


class Polygon:

	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.gca(projection='3d')
		
	def convert_color(self,arg):
	    return colorConverter.to_rgba(arg, alpha=0.6)

	def init(self,view):

		cube_points = np.arange(0, 10, 0.4)
		verts = []

		# number of polygons
		figures_num = [0.0, 1.0, 2.0, 3.0]

		for z in figures_num:
		    ys = np.random.rand(len(cube_points))
		    ys[0], ys[-1] = 0, 0
		    verts.append(list(zip(cube_points, ys)))

		    
		poly = PolyCollection(verts, facecolors=[self.convert_color('r'), self.convert_color('g'), self.convert_color('b'),
		                                         self.convert_color('y')])
		poly.set_alpha(0.7)
		self.ax.add_collection3d(poly, zs=figures_num, zdir='y')

		self.ax.set_xlabel('X')
		self.ax.set_xlim3d(0, 10)
		self.ax.set_ylabel('Y')
		self.ax.set_ylim3d(-1, 4)
		self.ax.set_zlabel('Z')
		self.ax.set_zlim3d(0, 1)

		if view == "image":
			savefig('polygon.png')
			print "Image saved on tredify folder"
		else:
			plt.show()

