import os 
import sys 
import string
import argparse

from lib import Parser, Bar, Scatter, Pie, AnimatedScatter

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='tredify: A Python framework to plot 2D and 3D structures and animations from JSON data.')
    parser.add_argument('-i', '--input', type=str, help='JSON file path', required=True)
    parser.add_argument('-t', '--type', type=str, help='Plot type', required=True,
                        choices=['bar', 'scatter', 'pie', 'animation'])
    parser.add_argument('-d', '--dimension', type=str, help='Plot Dimension',
                        required=False, choices=['2D', '3D'])
    parser.add_argument('-v', '--view', type=str, help='Visualize plot with GUI or Image',
                        required=True, choices=['gui', 'image'])
    parser.add_argument('-title', '--title', type=str, help='Pie plot title',
                        required=False)

    args = parser.parse_args()
 
    if args.type == 'Pie' and args.title == None:
        parser.error('If you want a Pie plot, you also have to set a title with -title argument')

    if args.type == "bar":
        parse_bar = Parser.ParseBar(args.input)
        dict_bar = parse_bar.process_data()

        if args.dimension == "2D":
            bar = Bar.Bar2D(dict_bar)
        else:
            bar = Bar.Bar(dict_bar)

        if args.view == "image":
            bar.init("image")
        else:
            bar.init("gui")

    elif args.type == "scatter":
        parse_scatter = Parser.ParseScatter(args.input)
        dict_scatter = parse_scatter.process_data()

        if args.dimension == "2D":
            scatter = Scatter.Scatter2D(dict_scatter)
        else:
            scatter = Scatter.Scatter(dict_scatter)

        if args.view == "image":
            scatter.init("image")
        else:
            scatter.init("gui")

    elif args.type == "pie":
        parse_pie = Parser.ParseBar(args.input)
        dict_pie = parse_pie.process_data()

        pie = Pie.Pie(dict_pie, args.title)

        if args.view == "image":
            pie.init("image")
        else:
            pie.init("gui")

    elif args.type == "animation":
        parse_scatter = Parser.ParseScatter(args.input)
        position_data = parse_scatter.process_data()

        if args.view != 'gui':
            parser.error('Storage of animation not supported yet')

        if args.dimension == "2D":
            animated_scatter = AnimatedScatter.AnimatedScatter2D(position_data)
        else:
            animated_scatter = AnimatedScatter.AnimatedScatter(position_data)

        animated_scatter.init()
