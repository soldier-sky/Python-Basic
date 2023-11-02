# Python code to illustrate the Modules

class Bmw: 
	# constructor to init the various models
	def __init__(self): 
		self.models = ['i7', 'x1', 'x5', 'x6'] 

	# A normal print function 
	def outModels(self): 
		print('These are the available models for BMW') 
		for model in self.models: 
			print('\t%s ' % model)

