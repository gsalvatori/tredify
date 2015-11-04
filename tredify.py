import os 
import sys 
import string
import argparse

sys.path.insert(0, 'lib/')
from Parser import *
from config import *
from Polygon import *
from Scatter import *
from Pie import *
from Bar import *


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='tredify: A Python framework to plot 2D and 3D structures from JSON data.')
	parser.add_argument('-i', '--input', type=str, help='JSON file path', required=True)
	parser.add_argument('-t', '--type', type=str, help='Plot type', required=True)
	parser.add_argument('-d', '--dimension', type=str, help='2D/3D', required=False)

	args = parser.parse_args()

	if args.type == "Bar":
		parse_bar = ParseBar(args.input)
		dict_bar = parse_bar.process_data()

		bar = Bar(dict_bar)
		bar.init()

	elif args.type == "Scatter":
		parse_scatter = ParseScatter(args.input)
		dict_scatter = parse_scatter.process_data()

		scatter = Scatter(dict_scatter)
		scatter.init()

	elif args.type == "Pie":
		parse_pie = ParseBar(args.input)
		dict_pie = parse_pie.process_data()

		pie = Pie(dict_pie,None)
		pie.init()



	
