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
    	print content





