import math
import queue
from node import Node
from edge import Edge

class Graph:

        """ Clase Grafo
        
                Atributos:
            id = Nombre genérico para identificar el grafo
            nodes = Lista de nodos que conforman el grafo
            edges = Lista de aristas que componen el grafo
            str_edges = Lista de aristas que componen el grafo 
                    en formato string(node1 -- node2)
        """
        
        def __init__(self):
                self.id = ""
                self.nodes = []
                self.edges = []
                self.str_edges = []

        def printGraph(self):
                
                """ Método para imprimir el grafo en consola """
                
                for i in range(len(self.edges)):
                        print(self.edges[i].id, self.edges[i].start, self.edges[i].end)
                for i in range(len(self.nodes)):
                        print(self.nodes[i].id, self.nodes[i].x,self.nodes[i].y)

        def addNode(self,id,x=0,y=0,label=""):
                
                """ Método para agregar un nodo al grafo """

                nod = Node(id,x,y,label)
                self.nodes.append(nod)

        def addEdge(self, id, start, end, weight=0):
                
                """ Método para agregar una arista al grafo """

                cur_edge= f"{start}--{end}"
                curv_edge= f"{end}--{start}"
                
                #verifica si el arista existe en el grafo, si no lo agrega
                if not( (cur_edge in self.str_edges) or (curv_edge in self.str_edges)):
                        e = Edge(id, start, end, weight)
                        self.edges.append(e)
                        self.str_edges.append(cur_edge)

        def getDegree(self, node):

                """ Calcula el grado del nodo """

                d=0
                for edge in self.edges:
                        if ((edge.start == node) or (edge.end == node) ):
                                d = d + 1
                return d

        def saveGraphViz(self, name):

                """ Exporta un archivo .gv que enumera los aristas del grafo """

                named = name +".gv"
                
                with open(named, 'w') as f:
                        f.write("graph " + name +  " {\n")

                        for edge in self.edges:
                                f.write(f"{edge.start} -- {edge.end} [label = {str(edge.weight)}];\n")

                        f.write("}\n")
        
        
        def clear(self):
            
            """ Vacía el grafo """
            
            self.nodes.clear()
            self.edges.clear()
            self.str_edges.clear()
            
            
        def neighbors(self, node):
            
            """ Encuentra los nodos vecinos de node que no estan marcados como visitados """
            
            neighbors = []
            
            for edge in self.edges:
                if (edge.start == node):
                    neighbors.append(edge.end)

                if (edge.end == node):
                    neighbors.append(edge.start)

            return neighbors
            
        
        def BFS(self, s):

            """ Método para aplicar BFS algorithm al grafo seleccionado
                    
                    Entrada:
                        s = Nodo raíz
                    
                    Salida:
                        BFS_tree = Árbol inducido por BFS Algorithm
            """
    
            BFS_Tree = Graph()
            q = queue.Queue()
            
            marked_nodes = []
            neighbors = []
            
            q.put(s)
            
            i=0
            while q.empty() != True:
                node = q.get()
                print(f"{node}\n")
                marked_nodes.append(node)
                neighbors = self.neighbors(node, marked_nodes)
                print(neighbors)
                for n in neighbors:
                    if n not in(marked_nodes):
                        e = Edge(i, node, n)
                        print (f"{i} = {node}, {n} \n")
                        BFS_Tree.edges.append(e)
                        marked_nodes.append(n)
                        q.put(n)
                        i = i + 1
                neighbors.clear()
                
            return BFS_Tree
        
        def DFS_R(self, s, marked_nodes, tree):
            
            """ Método para aplicar DFS recursivo al grafo seleccionado
                Nota: Siendo este un algoritmo recursivo, se tiene que dar de entrada
                una lista global de nodos visitados y un grafo global que terminará siendo el árbol
                inducido por DFS recursivo.
                    
                    Entrada:
                        s = Nodo raíz
                        marked_nodes = Lista de nodos ya visitados
                        tree = Árbol generado por las recursiones anteriores de DFS, inicia vacío.
                    
                    Salida:
                        tree = Árbol inducido por DFS Algorithm
            """
            
            neighbors = []
            
            node = s
            
            marked_nodes.append(node)
            
            neighbors = self.neighbors(node, marked_nodes)
            
            i=0
            for n in neighbors:
                if n not in(marked_nodes):
                    e = Edge(i, node, n)
                    tree.edges.append(e)
                    marked_nodes.append(n)
                    self.DFS_R(n, marked_nodes, tree) 
            neighbors.clear()
                
            return tree
            
                    
        def DFS_I(self, s):
            
            """ Método para aplicar DFS Iterativo al grafo seleccionado
                    
                    Entrada:
                        s = Nodo raíz
                    
                    Salida:
                        DFS_iTree = Árbol inducido por DFS Iterativo
            """
            
            DFS_iTree = Graph()
            
            stack = []
            stack.append(s)
            
            marked_nodes = []
            
            neighbors = []
            i=0
            while len(stack)>0:
                node = stack.pop()
                print(f"{node}\n")
                marked_nodes.append(node)
                neighbors = self.neighbors(node, marked_nodes)
                print(neighbors)
                j=0
                connected = False
                while connected !=True and len(neighbors)>0:
                    n = neighbors[j]
                    if n not in(marked_nodes):
                        e = Edge(i, node, n)
                        print (f"{i} = {node}, {n} \n")
                        DFS_iTree.edges.append(e)
                        marked_nodes.append(n)
                        stack.append(n)
                        connected = True
                        i = i + 1
                    
                    j=j+1
                neighbors.clear()
                
            return DFS_iTree
        
        def dfs(self,s):
                        
            """ Método para aplicar DFS a un grafo para verificar si hay ciclos en él 
                    
                    Entrada:
                        s = Nodo raíz
                    
                    Salida:
                        cycle = True or False
            """
            stack = []
            stack.append(s)
            
            marked_nodes = []
            cycle = False
            neighbors = []
            i=0
            while len(stack)>0 and cycle==False:
                node = stack.pop()
                print(node)

                print(marked_nodes)
                if node in(marked_nodes):
                    cycle = True
                else:
                    neighbors = self.neighbors(node)
                    print (neighbors)
                    for n in neighbors:
                        if n not in(marked_nodes):
                            stack.append(n)

                neighbors.clear()
                marked_nodes.append(node)
                print(cycle)
                print("end iteration")
            return cycle
        
        def Kruskal_D(self):
            """ Método para aplicar algoritmo directo de Kruskal a grafo
            
                Entrada:
                Salida:
                    total : (Impreso en consola) Peso total del árbol
                    MST: Minimun Spanning Tree inducido por el Kruskal Directo 
            """
            
            M = Graph()
            
            #Ordenar aristas de forma ascendente de acuerdo a su peso
            self.edges.sort(key=lambda value: value.weight)
            
            i=0
            #Verificar arista por arista en orden ascendente con respecto a su peso
            for edge in self.edges:
                
                #Verificar si el arista que se dese agregar generaría un ciclo                
                M.edges.append(edge)
                cycle = M.dfs(edge.start) 
                M.edges.pop()

                # Se agrega en caso que no genere un ciclo 
                if cycle == False:
                    M.addEdge(i,edge.start,edge.end,edge.weight)
                    i=i+1
                
            return M
