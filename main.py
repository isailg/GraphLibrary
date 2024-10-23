from graph import Graph
from node import Node
from edge import Edge
from algorithms import grafoErdosRenyi
from algorithms import grafoGilbert
from algorithms import grafoGeografico
from algorithms import grafoBarabasiAlbert
from algorithms import grafoDorogovtsevMendes
import random
"""
gER = grafoErdosRenyi(500,500)
gER.saveGraphViz("ErdosRenyi")

gGi = grafoGilbert(30,0.3)
gGi.saveGraphViz("Gilbert")

gGe = grafoGeografico(30,0.6)
gGe.saveGraphViz("GeograficoSimple")

gBA = grafoBarabasiAlbert(30,6)
gBA.saveGraphViz("BarabasiAlbert")
"""
gDM = grafoDorogovtsevMendes(30)
gDM.saveGraphViz("DorogovtsevMendes")


