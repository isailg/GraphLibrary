""" Programa principal
Ejecuta cada uno de los modelos de generación de grafos para 30,100 y 500 nodos, y exporta su archivo .gv correspondiente.
Por: Isaí López García
"""

from graph import Graph
from node import Node
from edge import Edge
from algorithms import *
import sys

if __name__ == "__main__":
    
    #Aumentando el limite de recursiones para DFS Recursivo
    sys.setrecursionlimit(15003)
    
    nlist = [30,100,500]
    
    for n in nlist:
        
        visited_nodes = []
        rDFS_tree = Graph()
        
        """ Erdos Renyi """
        #Generacion de grafo
        gER = grafoErdosRenyi(n,500, False)
        gER.saveGraphViz(f"GeneratedGraphs(.gv)/ErdosRenyi{n}")
        
        #Aplicando BFS
        BFS_ER = gER.BFS(12)
        BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{n}_BFS")
        
        #Aplicando DFS Recursivo
        gER.DFS_R(12, visited_nodes, rDFS_tree)
        rDFS_tree.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{n}_DFS_R")
        rDFS_tree.clear()
        visited_nodes.clear()
        
        #Aplicando DFS Iterativo
        ITree_ER = gER.DFS_I(12)
        ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi{n}_DFS_I")
        
        
        """ Gilbert """
        #Generacion de grafo
        gGi = grafoGilbert(n,0.3,False)
        gGi.saveGraphViz(f"GeneratedGraphs(.gv)/Gilbert{n}")
        
        #Aplicando BFS
        BFS_ER = gGi.BFS(12)
        BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert{n}_BFS")
        
        #Aplicando DFS Recursivo
        RTree_ER = gGi.DFS_R(12, visited_nodes, rDFS_tree)
        RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert{n}_DFS_R")
        rDFS_tree.clear()
        visited_nodes.clear()
        
        #Aplicando DFS Recursivo
        ITree_ER = gGi.DFS_I(12)
        ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert{n}_DFS_I")
        
        
        """ Malla """
        #Generacion de grafo
        gM = grafoMalla(n,30,False)
        gM.saveGraphViz(f"GeneratedGraphs(.gv)/Malla{n}")
        
        #Aplicando BFS
        BFS_ER = gM.BFS(12)
        BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Malla{n}_BFS")
        
        #Aplicando DFS Recursivo
        RTree_ER = gM.DFS_R(12, visited_nodes, rDFS_tree)
        RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Malla{n}_DFS_R")
        rDFS_tree.clear()
        visited_nodes.clear()
        
        #Aplicando DFS Recursivo
        ITree_ER = gM.DFS_I(12)
        ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/Malla{n}_DFS_I")
        
        
        """ Geografico Simple """
        #Generacion de grafo
        gGe = grafoGeografico(n,0.6,False)
        gGe.saveGraphViz(f"GeneratedGraphs(.gv)/GeograficoSimple{n}")
        
        #Aplicando BFS
        BFS_ER = gGe.BFS(12)
        BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple{n}_BFS")
        
        #Aplicando DFS Recursivo
        RTree_ER = gGe.DFS_R(12, visited_nodes, rDFS_tree)
        RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple{n}_DFS_R")
        rDFS_tree.clear()
        visited_nodes.clear()
        
        #Aplicando DFS Recursivo
        ITree_ER = gGe.DFS_I(12)
        ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple{n}_DFS_I")
        
        
        """ Barabasi Albert """
        #Generacion de grafo
        gBA = grafoBarabasiAlbert(n,6,False)
        gBA.saveGraphViz(f"GeneratedGraphs(.gv)/BarabasiAlbert{n}")
        
        #Aplicando BFS
        BFS_ER = gBA.BFS(12)
        BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert{n}_BFS")
        
        #Aplicando DFS Recursivo
        RTree_ER = gBA.DFS_R(12, visited_nodes, rDFS_tree)
        RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert{n}_DFS_R")
        rDFS_tree.clear()
        visited_nodes.clear()
        
        #Aplicando DFS Recursivo
        ITree_ER = gBA.DFS_I(12)
        ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert{n}_DFS_I")
        
        
        """ Dorogovtsev Mendes """
        #Generacion de grafo
        gDM = grafoDorogovtsevMendes(n,False)
        gDM.saveGraphViz(f"GeneratedGraphs(.gv)/DorogovtsevMendes{n}")
        
        #Aplicando BFS
        BFS_ER = gDM.BFS(12)
        BFS_ER.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes{n}_BFS")
        
        #Aplicando DFS Recursivo
        RTree_ER = gDM.DFS_R(12, visited_nodes, rDFS_tree)
        RTree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes{n}_DFS_R")
        rDFS_tree.clear()
        visited_nodes.clear()
        
        #Aplicando DFS Recursivo
        ITree_ER = gDM.DFS_I(12)
        ITree_ER.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes{n}_DFS_I")
