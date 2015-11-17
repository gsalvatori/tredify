import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import geojson
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
from mpl_toolkits.basemap import Basemap
from pylab import *
from random import *


class GIS:

	def __init__(self,dict_):
		self.coordinates = dict_["coordinates"]
		self.type = dict_["type"]

		# we set low resolution as default setting 
		self.map = Basemap(projection='merc',resolution='l')

	def point(self):
		self.map.drawcoastlines()
		self.map.drawcountries()
		self.map.fillcontinents(color = 'coral')
		self.map.drawmapboundary()

		x,y = self.map(self.coordinates[0],self.coordinates[1])
		self.map.plot(x, y, 'bo', markersize=10)
		 
		plt.show()

	def linestring(self):
		self.map.drawcoastlines()
		self.map.drawcountries()
		self.map.fillcontinents(color = 'coral')
		self.map.drawmapboundary()

		x,y = self.map(self.coordinates[0],self.coordinates[1])
		self.map.plot(x, y, color="green", linewidth=1.0, linestyle="-")
		 
		plt.show()


	def init(self):
		if self.type == "Point":
			self.point()
		elif self.type == "LineString":
			self.linestring()
