""" Programa principal
Ejecuta cada uno de los modelos de generación de grafos para 30,100 y 500 nodos, y exporta su archivo .gv correspondiente.
Por: Isaí López García
"""

from graph import Graph
from node import Node
from edge import Edge
from algorithms import *
import math

if __name__ == "__main__":
    
    nlist = [30, 300]
    namelist = ["pocos", "muchos"]
    k=0
    
    for n in nlist:
        
        c = namelist[k]
        
        """ Erdos Renyi """
        #Generacion de grafo
        gER = grafoErdosRenyi(n,n, False)
        gER.saveGraphViz(f"GeneratedGraphs(.gv)/ErdosRenyi_{c}({n})")
        
        #Aplicando Kruskal Directo
        MST1 = gER.Kruskal_D(f"ErdosRenyi_{c}({n})_Kruskal_D")
        MST1.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_Kruskal_D_{c}({n})")
        
        #Aplicando Kruskal Inverso
        MST2 = gER.Kruskal_I(f"ErdosRenyi_{c}({n})_Kruskal_I")
        MST2.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_Kruskal_I_{c}({n})")
        
        #Aplicando Prim algorithm
        MST3 = gER.Prim(f"ErdosRenyi_{c}({n})_Prim")
        MST3.saveGraphViz(f"CalculatedGraphs(.gv)/ErdosRenyi_Prim_{c}({n})")
        
        
        """ Gilbert """
        #Generacion de grafo
        gGi = grafoGilbert(n,0.3,False)
        gGi.saveGraphViz(f"GeneratedGraphs(.gv)/Gilbert_{c}({n})")
        
        #Aplicando Kruskal Directo
        MST4 = gGi.Kruskal_D(f"Gilbert_{c}({n})_Kruskal_D")
        MST4.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert_Kruskal_D_{c}({n})")
        
        #Aplicando Kruskal Inverso
        MST5 = gGi.Kruskal_I(f"Gilbert_{c}({n})_Kruskal_I")
        MST5.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert_Kruskal_I_{c}({n})")
        
        #Aplicando Prim algorithm
        MST6 = gGi.Prim(f"Gilbert_{c}({n})_Prim")
        MST6.saveGraphViz(f"CalculatedGraphs(.gv)/Gilbert_Prim_{c}({n})")
        
        
        """ Malla """
        #Generacion de grafo
        gM = grafoMalla(int(math.sqrt(n)),int(math.sqrt(n))+1,False)
        gM.saveGraphViz(f"GeneratedGraphs(.gv)/Malla_{c}({n})")
        
        #Aplicando Kruskal Directo
        MST7 = gM.Kruskal_D(f"Malla_{c}({n})_Kruskal_D")
        MST7.saveGraphViz(f"CalculatedGraphs(.gv)/Malla_Kruskal_D_{c}({n})")
        
        #Aplicando Kruskal Inverso
        MST8 = gM.Kruskal_I(f"Malla_{c}({n})_Kruskal_I")
        MST8.saveGraphViz(f"CalculatedGraphs(.gv)/Malla_Kruskal_I_{c}({n})")
        
        #Aplicando Prim algorithm
        MST9 = gM.Prim(f"Malla_{c}({n})_Prim")
        MST9.saveGraphViz(f"CalculatedGraphs(.gv)/Malla_Prim_{c}({n})")
        
        
        """ Geografico Simple """
        #Generacion de grafo
        gGe = grafoGeografico(n,0.6,False)
        gGe.saveGraphViz(f"GeneratedGraphs(.gv)/GeograficoSimple_{c}({n})")
        
        #Aplicando Kruskal Directo
        MST10 = gGe.Kruskal_D(f"GeograficoSimple_{c}({n})_Kruskal_D")
        MST10.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple_Kruskal_D_{c}({n})")
        
        #Aplicando Kruskal Inverso
        MST11 = gGe.Kruskal_I(f"GeograficoSimple_{c}({n})_Kruskal_I")
        MST11.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple_Kruskal_I_{c}({n})")
        
        #Aplicando Prim algorithm
        MST12 = gGe.Prim(f"GeograficoSimple_{c}({n})_Prim")
        MST12.saveGraphViz(f"CalculatedGraphs(.gv)/GeograficoSimple_Prim_{c}({n})")
        
        
        """ Barabasi Albert """
        #Generacion de grafo
        gBA = grafoBarabasiAlbert(n,6,False)
        gBA.saveGraphViz(f"GeneratedGraphs(.gv)/BarabasiAlbert_{c}({n})")
        
        #Aplicando Kruskal Directo
        MST13 = gBA.Kruskal_D(f"BarabasiAlbert_{c}({n})_Kruskal_D")
        MST13.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert_Kruskal_D_{c}({n})")
        
        #Aplicando Kruskal Inverso
        MST14 = gBA.Kruskal_I(f"BarabasiAlbert_{c}({n})_Kruskal_I")
        MST14.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert_Kruskal_I_{c}({n})")
        
        #Aplicando Prim algorithm
        MST15 = gBA.Prim(f"BarabasiAlbert_{c}({n})_Prim")
        MST15.saveGraphViz(f"CalculatedGraphs(.gv)/BarabasiAlbert_Prim_{c}({n})")
        
        
        """ Dorogovtsev Mendes """
        #Generacion de grafo
        gDM = grafoDorogovtsevMendes(n,False)
        gDM.saveGraphViz(f"GeneratedGraphs(.gv)/DorogovtsevMendes_{c}({n})")
        
        #Aplicando Kruskal Directo
        MST = gDM.Kruskal_D(f"DorogovtsevMendes_{c}({n})_Kruskal_D")
        MST.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes_Kruskal_D_{c}({n})")
        
        #Aplicando Kruskal Inverso
        MST = gDM.Kruskal_I(f"DorogovtsevMendes_{c}({n})_Kruskal_I")
        MST.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes_Kruskal_I_{c}({n})")
        
        #Aplicando Prim algorithm
        MST = gDM.Prim(f"DorogovtsevMendes_{c}({n})_Prim")
        MST.saveGraphViz(f"CalculatedGraphs(.gv)/DorogovtsevMendes_Prim_{c}({n})")
        
        k = k + 1
