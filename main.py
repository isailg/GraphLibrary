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
		
		gER = grafoErdosRenyi(n,100,False)
		gER.saveGraphViz(f"GeneratedGraphs(.gv)/ErdosRenyi{n}")
		
		"""
		BFS_ER = gER.BFS(12)
		BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{n}_BFS")
		
		explored_nodes = []
		DFS_Rtree = Graph()
		gER.DFS_R(12, explored_nodes, DFS_Rtree)
		DFS_Rtree.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{n}_DFS_R")
		DFS_Rtree.clear()
		explored_nodes.clear()
		
		ITree_ER = gER.DFS_I(12)
		ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{n}_DFS_I")
		"""
		
		gGi = grafoGilbert(n,0.3,False)
		gGi.saveGraphViz(f"GeneratedGraphs(.gv)/Gilbert{n}")
		
		"""			
		BFS_ER = gGi.BFS(12)
		BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert{n}_BFS")
		
		explored_nodes = []
		DFS_Rtree = Graph()
		RTree_ER = gGi.DFS_R(12, explored_nodes, DFS_Rtree)
		RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert{n}_DFS_R")
		DFS_Rtree.clear()
		explored_nodes.clear()
		
		ITree_ER = gGi.DFS_I(12)
		ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert{n}_DFS_I")
		"""	
		
		gM = grafoMalla(n,int(n/2),False)
		gM.saveGraphViz(f"GeneratedGraphs(.gv)/Malla{n}")
		
		"""	
		BFS_ER = gM.BFS(12)
		BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Malla{n}_BFS")
		
		explored_nodes = []
		DFS_Rtree = Graph()
		RTree_ER = gM.DFS_R(12, explored_nodes, DFS_Rtree)
		RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Malla{n}_DFS_R")
		DFS_Rtree.clear()
		explored_nodes.clear()
		
		ITree_ER = gM.DFS_I(12)
		ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Malla{n}_DFS_I")
		"""
		
		gGe = grafoGeografico(n,0.6,False)
		gGe.saveGraphViz(f"GeneratedGraphs(.gv)/GeograficoSimple{n}")
		
		"""
		BFS_ER = gGe.BFS(12)
		BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple{n}_BFS")
		
		explored_nodes = []
		DFS_Rtree = Graph()
		RTree_ER = gGe.DFS_R(12, explored_nodes, DFS_Rtree)
		RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple{n}_DFS_R")
		DFS_Rtree.clear()
		explored_nodes.clear()
		
		ITree_ER = gGe.DFS_I(12)
		ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple{n}_DFS_I")
		"""
		
		gBA = grafoBarabasiAlbert(n,6,False)
		gBA.saveGraphViz(f"GeneratedGraphs(.gv)/BarabasiAlbert{n}")
		
		"""	
		BFS_ER = gBA.BFS(12)
		BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert{n}_BFS")
		
		explored_nodes = []
		DFS_Rtree = Graph()
		RTree_ER = gBA.DFS_R(12, explored_nodes, DFS_Rtree)
		RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert{n}_DFS_R")
		DFS_Rtree.clear()
		explored_nodes.clear()
		
		ITree_ER = gBA.DFS_I(12)
		ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert{n}_DFS_I")
		"""
		
		gDM = grafoDorogovtsevMendes(n,False)
		gDM.saveGraphViz(f"GeneratedGraphs(.gv)/DorogovtsevMendes{n}")
		
		"""
		BFS_ER = gDM.BFS(12)
		BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes{n}_BFS")
		
		explored_nodes = []
		DFS_Rtree = Graph()
		RTree_ER = gDM.DFS_R(12, explored_nodes, DFS_Rtree)
		RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes{n}_DFS_R")
		DFS_Rtree.clear()
		explored_nodes.clear()
		
		ITree_ER = gDM.DFS_I(12)
		ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes{n}_DFS_I")
		"""
