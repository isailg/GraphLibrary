from graph import Graph
from node import Node
from edge import Edge
import random


def grafoMalla(m, n, directed: False):
	"""
	Genera grafo de malla
	Entrada:
		m: número de columnas (>1)
		n: número de filas (>1)
		directed: Es dirigido o no
	Salida:
		Grafo
	"""


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
	
def grafoGeografico(n, r, directed: False):
	"""
	Genera grafo aleatorio con el modelo geográfico simple
	Entrada:
		n: número de nodos (>0)
		r: distancia máxima para crear un nodo [0,1]
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
	
def grafoBarabasiAlbert(n, d, directed: False):
	"""
	Genera grafo aleatorio con el modelo Barabasi-Albert
	Entrada:
		n: número de nodos (>0)
		d: grado máximo esperado por cada nodo (>1)
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
	

def grafoDorogovtsevMendes(n, directed: False):
	"""
	Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
	Entrada:
		n: número de nodos (>=3)
		directed: Es dirigido o no
	Salida:
		Grafo
	""" 
