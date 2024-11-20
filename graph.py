import math


from node import Node
from edge import Edge

class Graph:
	"""
	Clase Grafo
		Atributos:
			id = Nombre genérico para identificar el grafo
			nodes = Lista de nodos que conforman el grafo
			edges = Lista de aristas que componen el grafo
			str_edges = Lista de aristas que componen el grafo 
					en formato string(node1 -- node2)
	"""
	
	def __init__(self):
		
		self.id = ""
		self.nodes = []
		self.edges = []
		self.str_edges = []
		
	def printGraph(self):
		"""
		Método para imprimir el grafo en consola
		"""
		for i in range(len(self.edges)):
			print(self.edges[i].id, self.edges[i].start, self.edges[i].end)
			
		for i in range(len(self.nodes)):
			print(self.nodes[i].id, self.nodes[i].x,self.nodes[i].y)
		
	def addNode(self,id,x=0,y=0):
		"""
		Método para agregar un nodo al grafo
		"""
		nod = Node(id,x,y)
		self.nodes.append(nod)
	
	def addEdge(self, id, start, end):
		"""
		Método para agregar una arista al grafo
		"""
		cur_edge= f"{start}--{end}"
		curv_edge= f"{end}--{start}"
		
		#verifica si el arista existe en el grafo
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
		Exporta un archivo .gv que enumera los aristas del grafo
		"""
		named = "GraphViz/"+ name +".gv"
		with open(named, 'w') as f:
			f.write("graph " + name +  " {\n")
			
			for edge in self.edges:
				f.write(f"{edge.start} -- {edge.end};\n")
				
			f.write("}\n")

		
