import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from mpl_toolkits.mplot3d import Axes3D
from pylab import *


class Pie:

	def __init__(self,dict_,title):
		figure(1, figsize=(6,6))
		self.ax = axes([0.1, 0.1, 0.8, 0.8])
		self.dict = dict_
		self.title = title

	def get_labels(self):
		labels = []
		for i in range(0,len(self.dict)):
			labels.append(self.dict[i]["LABEL"])

		return labels

	def get_fractions(self):
		fractions = []
		for i in range(0,len(self.dict)):
			fractions.append(self.dict[i]["PERCENTAGE"])

		return fractions

	def get_exploded_pieces(self):
		exploded = []

		for i in range(0,len(self.dict)):
			item = self.dict[i]["EXPLODE"]
			if item == "True":
				exploded.append(0.5)
			else:
				exploded.append(0)
				
		return exploded

	def init(self):
		labels = self.get_labels()
		fracs = self.get_fractions()

		# generating explode...
		explode = self.get_exploded_pieces()

		pie(fracs, explode=explode, labels=labels,
		                autopct='%1.1f%%', shadow=True, startangle=90)

		title(self.title, bbox={'facecolor':'0.8', 'pad':5})

		show()

		
