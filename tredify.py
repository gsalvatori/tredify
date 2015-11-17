import os 
import sys 
import string
import argparse

sys.path.insert(0, 'lib/')
from Parser import *
from Polygon import *
from Scatter import *
from Pie import *
from Bar import *
from GIS import *


if __name__ == '__main__':
	
	### Standard parser arguments ###
	parser = argparse.ArgumentParser(description='tredify: A Python framework to plot 2D and 3D structures from JSON data.')
	parser.add_argument('-i', '--input', type=str, help='JSON file path', required=True)
	parser.add_argument('-t', '--type', type=str, help='Plot type', required=False, choices=['bar','scatter','pie'])
	parser.add_argument('-d', '--dimension', type=str, help='Plot Dimension', required=False, choices=['2D','3D'])
	parser.add_argument('-v', '--view', type=str, help='Visualize plot with GUI or Image', required=False, choices=['gui','image'])
	parser.add_argument('-title', '--title', type=str, help='Pie plot title', required=False)
	args = parser.parse_args()
	#################################
	
	### GIS subparser for -gis argument ###

	#######################################
 
	if args.type == 'Pie' and args.title == None:
		parser.error('If you want a Pie plot, you also have to set a title with -title argument')

	if args.type == "bar":
		parse_bar = ParseBar(args.input)
		dict_bar = parse_bar.process_data()

		if args.dimension == "2D":
			bar = Bar2D(dict_bar)
		else:
			bar = Bar(dict_bar)

		if args.view == "image":
			bar.init("image")
		else:
			bar.init("gui")

	elif args.type == "scatter":
		parse_scatter = ParseScatter(args.input)
		dict_scatter = parse_scatter.process_data()

		if args.dimension == "2D":
			scatter = Scatter2D(dict_scatter)
		else:
			scatter = Scatter(dict_scatter)

		if args.view == "image":
			scatter.init("image")
		else:
			scatter.init("gui")

	elif args.type == "pie":
		parse_pie = ParseBar(args.input)
		dict_pie = parse_pie.process_data()

		if args.dimension == "2D":
			pie = Pie2D(dict_pie,args.title)
		else:
			pie = Pie(dict_pie,args.title)

		if args.view == "image":
			pie.init("image")
		else:
			pie.init("gui")
