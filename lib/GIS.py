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
		self.map = Basemap(projection='merc',resolution='h')

	def point(self):
		self.map.drawcoastlines()
		self.map.drawcountries()
		self.map.fillcontinents(color = 'coral')
		self.map.drawmapboundary()

		x,y = self.map(self.coordinates[0],self.coordinates[1])
		self.map.plot(x, y, 'bo', markersize=10)
		 
		plt.show()

	def init(self):
		self.point()
