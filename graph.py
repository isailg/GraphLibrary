import math


from node import Node
from edge import Edge

class Graph:
	
	
	def __init__(self):
		
		self.id = "graph"
		self.nodes = []
		self.edges = []
		
	def imprimir(self):
		for i in range(len(self.edges)):
			print(self.edges[i].id, self.edges[i].start, self.edges[i].end )
			
		for i in range(len(self.nodes)):
			print(self.nodes[i].id, self.nodes[i].x,self.nodes[i].y)
		
	def addNode(self,id):
		"""
		Agregar nodo al grafo
		"""
		nod = Node(id)
		self.nodes.append(nod)
	
	def addEdge(self, id, start, end):
		"""
		Agregar una arista
		"""

		e = Edge(id, start, end)
		self.edges.append(e)
		
		
