import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import geojson
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter
from pylab import *
from random import *


class GIS:

	def __init__(self,dict_):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111, projection='3d')
		self.dict = dict_
