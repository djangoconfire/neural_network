import numpy as np 

class BackPropogationNetwork:
	""" A BackPropogation Network """

	# class Member
	layer_count=0
	shape=None
	weights=[]

	# class Methods

	def __init__(self, layer_size):
		""" Initiaze the network here """

		# layer info
		self.layer_count=len(layer_size) - 1
		self.shape=layer_size

		# input and output data
		self._input_data=[]
		self._output_data=[]

		# weight matrices
		for i,j in zip(layer_size[:-1],layer_size[1:]):
			self.weights.append(np.random.normal(scale=0.1,size=(j,i+1)))


if __name__=='__main__':
	bpn=BackPropogationNetwork((2,2,1))
	print bpn.weights
			

