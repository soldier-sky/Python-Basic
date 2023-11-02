# Python code to illustrate the Modules

class Tata: 
	# constructor to init the various models
	def __init__(self): 
		self.models = ['Tigor', 'Nexon', 'Harrier', 'Safari'] 

	# A normal print function 
	def outModels(self): 
		print('These are the available models for Tata') 
		for model in self.models: 
			print('\t%s ' % model) 
