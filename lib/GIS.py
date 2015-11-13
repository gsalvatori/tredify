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
		# make up some data on a regular lat/lon grid.
		nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
		lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
		lons = (delta*np.indices((nlats,nlons))[1,:,:])
		wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
		mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
		# compute native map projection coordinates of lat/lon grid.
		x, y = self.map(lons*180./np.pi, lats*180./np.pi)
		# contour data over the map.
		cs = self.map.contour(x,y,wave+mean,15,linewidths=1.5)
		plt.title('contour lines over filled continent background')
		plt.show()

	def init(self):
		self.point()
