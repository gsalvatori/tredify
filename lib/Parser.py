import os
import sys
import json

class Parser:
	def __init__(self,filename):
		self.file = filename

	def load_json(self):
		with open(self.file) as data_file:    
			data = json.load(data_file)
		return data


class ParseScatter(Parser):
    def __init__(self,filename):
        Parser.__init__(self, filename)
        self.file = filename

    def process_data(self):
    	parse = Parser(self.file)
    	content = parse.load_json()
    	return content


class ParsePie(Parser):
    def __init__(self,filename):
        Parser.__init__(self, filename)
        self.file = filename

    def process_data(self):
        parse = Parser(self.file)
        content = parse.load_json()

        total_percentage = 0
        for i in range(0,len(content)):
            total_percentage += content[i]["PERCENTAGE"]
        
        if total_percentage == 100:
            return content
        else:
            print "[ ERROR ] Total percentage must be equal to 100"


class ParseBar(Parser):
    def __init__(self,filename):
        Parser.__init__(self, filename)
        self.file = filename

    def process_data(self):
        parse = Parser(self.file)
        content = parse.load_json()

        return content








