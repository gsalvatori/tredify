import os 
import sys 
import string


sys.path.insert(0, '../lib/')
from Parser import *
from Polygon import *
from Scatter import *
from Pie import *
from Bar import *


if __name__ == '__main__':
    
    test_pie = ParsePie("../json/pie.json")
    test_bar = ParseBar("../json/bar.json")
    test_scat = ParseScatter("../json/scatter.json")

    dict_pie = test_pie.process_data()
    dict_bar = test_bar.process_data()
    dict_scat = test_scat.process_data()

    pie = Pie(dict_pie,"Movies")
    bar = Bar(dict_bar)
    scat = Scatter(dict_scat)
