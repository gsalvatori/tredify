import os 
import sys 
import string
import argparse

sys.path.insert(0, '../lib/')
from Parser import *
from Polygon import *
from Scatter import *
from Pie import *
from Bar import *
from GIS import *


if __name__ == '__main__':
	
	parse_GIS = Parser('../json/geojson.json')
	dict_gis = parse_GIS.load_json()

	point = GIS(dict_gis)
	point.init()
