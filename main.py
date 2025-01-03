""" Programa principal
Ejecuta cada uno de los modelos de generación de grafos para 30 y 100 nodos, aplica el algoritmo Dijkstra y exporta su archivo .gv correspondiente.
Por: Isaí López García
"""

from graph import Graph
from node import Node
from edge import Edge
from algorithms import *
import sys
import math

if __name__ == "__main__":
    
    nlist = [30,100]
    namelist = ["pocos", "muchos"]
    k=0
    
    for n in nlist:
        
        c = namelist[k]
        
        """ Erdos Renyi """
        #Generacion de grafo
        gER = grafoErdosRenyi(n,n, False)
        gER.saveGraphViz(f"GeneratedGraphs(.gv)/ErdosRenyi_{c}({n})")
        
        #Aplicando Dijkstra
        S = gER.dijkstra(0)
        S.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_{c}({n})_Dijkstra")

        
        """ Gilbert """
        #Generacion de grafo
        gGi = grafoGilbert(n,0.3,False)
        gGi.saveGraphViz(f"GeneratedGraphs(.gv)/Gilbert_{c}({n})")
        
        #Aplicando Dijkstra
        S1 = gGi.dijkstra(0)
        S1.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert_{c}({n})_Dijkstra")
        
        
        """ Malla """
        #Generacion de grafo
        gM = grafoMalla(int(math.sqrt(n)),int(math.sqrt(n)),False)
        gM.saveGraphViz(f"GeneratedGraphs(.gv)/Malla_{c}({n})")
        
        #Aplicando Dijkstra
        S2 = gM.dijkstra(0)
        S2.saveGraphViz(f"CalculatedGraphs(.gv)/Malla_{c}({n})_Dijkstra")
        
        
        """ Geografico Simple """
        #Generacion de grafo
        gGe = grafoGeografico(n,0.6,False)
        gGe.saveGraphViz(f"GeneratedGraphs(.gv)/GeograficoSimple_{c}({n})")
        
        #Aplicando Dijkstra
        S3 = gGe.dijkstra(0)
        S3.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple_{c}({n})_Dijkstra")
        
        
        """ Barabasi Albert """
        #Generacion de grafo
        gBA = grafoBarabasiAlbert(n,6,False)
        gBA.saveGraphViz(f"GeneratedGraphs(.gv)/BarabasiAlbert_{c}({n})")
        
        #Aplicando Dijkstra
        S4 = gBA.dijkstra(0)
        S4.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert_{c}({n})_Dijkstra")
        
        
        """ "Dorogovtsev Mendes """
        #Generacion de grafo
        gDM = grafoDorogovtsevMendes(n,False)
        gDM.saveGraphViz(f"GeneratedGraphs(.gv)/DorogovtsevMendes_{c}({n})")
        
        #Aplicando Dijkstra
        S5 = gDM.dijkstra(0)
        S5.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes_{c}({n})_Dijkstra")
        
        k = k + 1
