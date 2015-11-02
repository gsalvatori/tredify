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
	
	test = ParseScatter("/home/gabriele/Scrivania/tredify/json/scatter.json")
	dict_ = test.process_data()

	scatter = Scatter(dict_)
	scatter.init()
