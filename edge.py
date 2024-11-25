import math

class Edge:
    """ Clase Arista

                Atributos:
            id = Número entero identificador
            start = Nodo de inicio del arista
            end = Nodo final del arista
                        color = Color del arista
                        label = Etiqueta del arista
    """
        
    def __init__(self, id, start=0, end=0, color=0, label=""):

                self.id = id
                self.start = start
                self.end = end
                self.color = color
                self.label = label
    

