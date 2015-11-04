import os 
import sys 
import random
import string
import time
import threading

sys.path.insert(0, 'lib/')
from Parser import *
from config import *
from Polygon import *
from Scatter import *


if __name__ == '__main__':
	
	test = ParsePie("/home/gabriele/Scrivania/tredify/json/pie.json")
	dict_ = test.process_data()

	print dict_
	# pie = Pie(dict_)
	# pie.init()
