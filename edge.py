import math

class Edge:
	"""
	Clase Arista
		Atributos:
			id = Número entero identificador
			start = Nodo de inicio del arista
			end = Nodo final del arista
	"""
	def __init__(self, id, start=0, end=0):
		
		self.id = id
		self.start = start
		self.end = end
	

