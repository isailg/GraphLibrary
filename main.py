"""
Programa principal
Ejecuta cada uno de los modelos de generación de grafos para 30,100 y 500 nodos, y exporta su archivo .gv correspondiente.
Por: Isaí López García
"""

from graph import Graph
from node import Node
from edge import Edge
from algorithms import *

if __name__ == "__main__":
	
	
	nlist = [30,100,500]
	
	for n in nlist:
	
		gER = grafoErdosRenyi(n,30,False)
		gER.saveGraphViz(f"GeneratedGraphs(.gv)/ErdosRenyi{n}")
		explored_nodes = []
		DFS_Rtree = Graph()
		
		Tree_ER = gER.DFS_R(0, explored_nodes, DFS_Rtree)
		Tree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{n}_DFS_R")
"""
		gGi = grafoGilbert(n,0.3,False)
		gGi.saveGraphViz(f"Gilbert{n}")
		
		gM = grafoMalla(n,int(n/2),False)
		gM.saveGraphViz(f"Malla{n}")

		gGe = grafoGeografico(n,0.6,False)
		gGe.saveGraphViz(f"GeograficoSimple{n}")

		gBA = grafoBarabasiAlbert(n,6,False)
		gBA.saveGraphViz(f"BarabasiAlbert{n}")

		gDM = grafoDorogovtsevMendes(n,False)
		gDM.saveGraphViz(f"DorogovtsevMendes{n}")
		
"""

