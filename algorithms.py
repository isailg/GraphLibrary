from graph import Graph
from node import Node
from edge import Edge
import random
from math import sqrt


def grafoMalla(m, n, directed= False):
	"""
	Genera grafo de malla
	Entrada:
		m: número de columnas (>1)
		n: número de filas (>1)
		directed: Es dirigido o no
	Salida:
		Grafo
	"""
	graph = Graph()

	c=[]
	index=0
	for i in range(m):
		for j in range(n):
			c=[i,j]
			graph.addNode(index,c)
			index = index + 1
	c=[]
	index=0
	for i in range(m):
		for j in range(n):
			node = index
			if (i<=m-2 and j<=n-2):
				node_right = index + 1
				node_bottom = (i+1)*n + j
				graph.addEdge(index,node,node_right)
				graph.addEdge(index,node,node_bottom)
				index = index + 1
				
			if(j==n-1 and i!=m-1):
				node_bottom = (i+1)*n + j
				graph.addEdge(index,node,node_bottom)
				index = index + 1
			
			if(i==m-1 and j!=n-1):
				node_right = index + 1
				graph.addEdge(index,node,node_right)
				index = index + 1
		
	
			
	return graph


def grafoErdosRenyi(n, m, directed= False):
	"""
	Genera grafo aleatorio con el modelo Erdos-Renyi
	Entrada:
		n: número de nodos (>0)
		m: número de aristas (>=n-1)
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
	graph = Graph()
	
	for i in range (n):
		graph.addNode(i)
		
	for i in range(m):
		n1 = random.randint(0,n-1)
		n2 = random.randint(0,n-1)
		if n1 != n2:
			graph.addEdge(i,n1,n2)
			
	return graph
		
		
def grafoGilbert(n, p, directed= False):
	"""
	Genera grafo aleatorio con el modelo Gilbert
	Entrada:
		n: número de nodos (>0)
		p: probabilidad para crear un arista [0,1]
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
	graph = Graph()
	
	for i in range(n):
		graph.addNode(i)
	c = 0
	for i in range(n):
		for j in range(n):
			if (random.random()<=p):
				graph.addEdge(c,i,j)
				c = c + 1
	return graph
	
	
def grafoGeografico(n, r, directed= False):
	"""
	Genera grafo aleatorio con el modelo geográfico simple
	Entrada:
		n: número de nodos (>0)
		r: distancia máxima para crear un nodo [0,1]
		directed: Es dirigido o no
	Salida:
		Grafo
	"""
	graph = Graph()
	
	for i in range(n):
		x = random.random()
		y = random.random()
		graph.addNode(i,x,y)
		
	c = 0
	for i in range(n):
		x1 = graph.nodes[i].x
		y1 = graph.nodes[i].y
		for j in range(n):
			x2 = graph.nodes[j].x
			y2 = graph.nodes[j].y
	
			dist = sqrt((x2-x1)**2+(y2-y1)**2)
			
			if (dist<=r):
				graph.addEdge(c,i,j)
				c = c + 1
	return graph



def grafoBarabasiAlbert(n, d, directed= False):
	"""
	Genera grafo aleatorio con el modelo Barabasi-Albert
	Entrada:
		n: número de nodos (>0)
		d: grado máximo esperado por cada nodo (>1)
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
	graph = Graph()
	

	graph.addNode(0)
	c = 2
	for i in range(1,n):
		graph.addNode(i)
		randomNodes = random.sample(range(i),i)
				
		for j in range(i):

			node = graph.nodes[randomNodes[j]]		
			deg = graph.getDegree(node)
			p = 1 - deg / d		
			
			
			if random.random() <= p:
				if (i!=randomNodes[j]):
					graph.addEdge(c,i,randomNodes[j])
					c = c + 1
			
	return graph

def grafoDorogovtsevMendes(n, directed= False):
	"""
	Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
	Entrada:
		n: número de nodos (>=3)
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
	
	graph = Graph()
	

	for i in range(3):
		graph.addNode(i)

	graph.addEdge(0,0,1)
	graph.addEdge(1,1,2)
	graph.addEdge(2,2,0)
	
	c=3
	for i in range(3,n):
		
		graph.addNode(i)
		
		random_edge = random.randint(0,i-1)
		
		node1 = graph.edges[random_edge].start
		node2 = graph.edges[random_edge].end
		
		graph.addEdge(c,i,node1)
		graph.addEdge(c+1,i,node2)
		
		c = c + 2
		
	
			
	return graph
