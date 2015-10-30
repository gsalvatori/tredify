import os 
import sys 
import random
import string
import time
import threading

sys.path.insert(0, 'lib/')
from config import *
from Polygon import *
from Scatter import *


if __name__ == '__main__':
	# polygon = Polygon()
	# polygon.init()
	scatter = Scatter()
	scatter.init()