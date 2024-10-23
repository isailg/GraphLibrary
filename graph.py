import math


from node import Node
from edge import Edge

class Graph:
	
	
	def __init__(self):
		
		self.id = "graph"
		self.nodes = []
		self.edges = []
		self.str_edges = []
		
	def printGraph(self):
		for i in range(len(self.edges)):
			print(self.edges[i].id, self.edges[i].start, self.edges[i].end)
			
		for i in range(len(self.nodes)):
			print(self.nodes[i].id, self.nodes[i].x,self.nodes[i].y)
		
	def addNode(self,id,x=0,y=0):
		"""
		Agregar nodo al grafo
		"""
		nod = Node(id,x,y)
		self.nodes.append(nod)
	
	def addEdge(self, id, start, end):
		"""
		Agregar una arista
		"""
		cur_edge= f"{start}--{end}"
		curv_edge= f"{end}--{start}"

		if not( (cur_edge in self.str_edges) or (curv_edge in self.str_edges)):
						
			e = Edge(id, start, end)
			self.edges.append(e)
			self.str_edges.append(cur_edge)
			
	def getDegree(self, node):
		"""
		Calcula el grado del nodo
		"""
		d=0
		for edge in self.edges:
			if ((edge.start == node) or (edge.end == node) ):
				d = d + 1

		return d
		
	def saveGraphViz(self, name):
		"""
		
		"""
		name = "GraphViz/"+ name +".gv"
		with open(name, 'w') as f:
			f.write("graph G {\n")
			
			for node in self.nodes:
				f.write(f"{node.id};\n")
			for edge in self.edges:
				f.write(f"{edge.start}--{edge.end};\n")
				
			f.write("}\n")

		
