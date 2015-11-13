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
		self.map = Basemap(projection='ortho',lat_0=self.coordinates[0],lon_0=self.coordinates[1],resolution='l')

	def point(self):
		x,y = self.map(self.coordinates[0],self.coordinates[1])
		my_map.plot(x, y, 'bo', markersize=12)

		plt.show()

	def init(self):
		self.point()
