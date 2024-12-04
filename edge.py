import math

class Edge:
    """ Clase Arista

                Atributos:
            id = Número entero identificador
            start = Nodo de inicio del arista
            end = Nodo final del arista
            weight = Peso del nodo
            label = Etiqueta del arista
    """
        
    def __init__(self, id, start=0, end=0, weight=0, label=""):

                self.id = id
                self.start = start
                self.end = end
                self.weight = weight
                self.label = label
    

