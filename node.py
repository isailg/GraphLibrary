import math

class Node:
	"""
	Clase Nodo
		Atributos:
			id = Número entero identificador
			x = Coordenada x del nodo para usarlo en 
			    métodos que lo requieran.
			y = Coordenada y del nodo para usarlo en 
			    métodos que lo requieran.
	"""
	def __init__(self, id, x=0, y=0):
		
		self.id = id
		self.x = x
		self.y = y
