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
from Pie import *
from Bar import *


if __name__ == '__main__':
	
	test = ParseBar("/home/gabriele/Scrivania/tredify/json/bar.json")
	dict_ = test.process_data()

	bar = Bar(dict_)
	bar.init()
	
