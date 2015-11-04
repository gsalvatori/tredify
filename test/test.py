import os 
import sys 
import string


sys.path.insert(0, '../lib/')
from Parser import *
from config import *
from Polygon import *
from Scatter import *
from Pie import *
from Bar import *


if __name__ == '__main__':
	
	test_pie  = ParsePie("/home/gabriele/Scrivania/tredify/json/pie.json")
	test_bar  = ParseBar("/home/gabriele/Scrivania/tredify/json/bar.json")
	test_scat = ParseScatter("/home/gabriele/Scrivania/tredify/json/scatter.json")

	dict_pie = test_pie.process_data()
	dict_bar = test_bar.process_data()
	dict_scat = test_scat.process_data()

	pie  = Pie(dict_pie,"Movies")
	bar  = Bar(dict_bar)
	scat = Scatter(dict_scat)

	
