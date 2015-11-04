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


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='tredify: A Python framework to plot 2D and 3D structures from JSON data.')
	parser.add_argument('-i', '--input', type=str, help='JSON file path', required=True)
	parser.add_argument('-t', '--type', type=str, help='Plot type (Bar,Scatter,Pie)', required=True)
	parser.add_argument('-d', '--dimension', type=str, help='Plot Dimension (2D,3D)', required=False)
	parser.add_argument('-v', '--view', type=str, help='Visualize plot with GUI or Image(GUI,Image)', required=True)
	parser.add_argument('-title', '--title', type=str, help='Pie plot title', required=False)

	args = parser.parse_args()
 
	if args.type == 'Pie' and args.title == None:
		parser.error('If you want a Pie plot, you also have to set a title with -title argument')

	if args.type == "Bar":
		parse_bar = ParseBar(args.input)
		dict_bar = parse_bar.process_data()

		bar = Bar(dict_bar)
		if args.view == "Image":
			bar.init("Image")
		bar.init("GUI")

	elif args.type == "Scatter":
		parse_scatter = ParseScatter(args.input)
		dict_scatter = parse_scatter.process_data()

		scatter = Scatter(dict_scatter)

		if args.view == "Image":
			scatter.init("Image")
		scatter.init("GUI")

	elif args.type == "Pie":
		parse_pie = ParseBar(args.input)
		dict_pie = parse_pie.process_data()

		pie = Pie(dict_pie,args.title)

		if args.view == "Image":
			pie.init("Image")
		pie.init("GUI")




	
