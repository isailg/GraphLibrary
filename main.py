""" Programa principal
Ejecuta cada uno de los modelos de generación de grafos para 100 y 500 nodos, visualiza el grafo mediante el método Spring escrito con pygame y guarda automáticamente el video con OpenCV.
Por: Isaí López García
"""

from graph import Graph
from node import Node
from edge import Edge
from algorithms import *
from graph_visualizer import App
import math



if __name__ == "__main__":
    
    nlist = [100]
    
    # Iniciando Pygame App para visualizar grafos
    Graph_visualizer = App()
    
    for n in nlist:
        
        """ Erdos Renyi 
        #Generacion de grafo
        gER = grafoErdosRenyi(n, int(n/2) ,False)
        gER.saveGraphViz(f"GeneratedGraphs(.gv)/ErdosRenyi{n}")

        #Aplicando Metodo Spring para Disposicion de Grafos
        Graph_visualizer.on_execute(gER, f"ErdosRenyi{n}_Fruchterman-Reingold")
        """
                
        """ Gilbert 
        #Generacion de grafo
        gGi = grafoGilbert(n,0.3,False)
        gGi.saveGraphViz(f"GeneratedGraphs(.gv)/Gilbert{n}")
        
        #Aplicando Metodo Spring para Disposicion de Grafos
        Graph_visualizer.on_execute(gGi, f"Gilbert{n}")
        """
        
        """ Malla 
        #Generacion de grafo
        gM = grafoMalla(int(math.sqrt(n)), int(math.sqrt(n))+1,False)
        gM.saveGraphViz(f"GeneratedGraphs(.gv)/Malla{n}")
                
        #Aplicando Metodo Spring para Disposicion de Grafos
        Graph_visualizer.on_execute(gM, f"Malla{n}")
        """
        
        """ Geografico Simple 
        #Generacion de grafo
        gGe = grafoGeografico(n,0.6,False)
        gGe.saveGraphViz(f"GeneratedGraphs(.gv)/GeograficoSimple{n}")
        
        #Aplicando Metodo Spring para Disposicion de Grafos
        Graph_visualizer.on_execute(gGe, f"Geografico{n}")
        """
        
        """ Barabasi Albert """
        #Generacion de grafo
        gBA = grafoBarabasiAlbert(n,6,False)
        gBA.saveGraphViz(f"GeneratedGraphs(.gv)/BarabasiAlbert{n}")
        
        #Aplicando Metodo Spring para Disposicion de Grafos
        Graph_visualizer.on_execute(gBA, f"BarabasiAlbert{n}")
        
        """ Dorogovtsev Mendes 
        #Generacion de grafo
        gDM = grafoDorogovtsevMendes(n,False)
        gDM.saveGraphViz(f"GeneratedGraphs(.gv)/DorogovtsevMendes{n}")
        
        #Aplicando Metodo Spring para Disposicion de Grafos
        Graph_visualizer.on_execute(gDM, f"DorogovtsevMendes{n}")
        """
