import math

class Node:

        """ Clase Nodo

                Atributos:
            id = Número entero identificador
            x = Coordenada x del nodo para usarlo en 
                métodos que lo requieran.
            y = Coordenada y del nodo para usarlo en 
                métodos que lo requieran.
                        color = Color del nodo
                        label = Etiqueta del nodo (string)
    """

        def __init__(self, id, x=0, y=0, color=0, label=""):

                self.id = id
                self.x = x
                self.y = y
                self.color = color
                self.label = label
