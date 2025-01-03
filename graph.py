import math
import queue
from node import Node
from edge import Edge
import heapq

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
                neighbors = self.neighbors(node)
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
            print(f"{node}\n")
            
            marked_nodes.append(node)
            
            neighbors = self.neighbors(node)
            
            print(neighbors)
            i=0
            for n in neighbors:
                if n not in(marked_nodes):
                    e = Edge(i, node, n)
                    print (f"{i} = {node}, {n} \n")
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
            
            marked_nodes = set()
            
            neighbors = []
            i=0
            while len(stack)>0:
                print(stack)
                node = stack.pop()
                print(f"{node}\n")
                marked_nodes.add(node)
                neighbors = self.neighbors(node)
                print(neighbors)

                for n in neighbors:
                    if n not in(marked_nodes):
                        e = Edge(i, node, n)
                        print (f"Edge{i} = {node}, {n} \n")
                        DFS_iTree.edges.append(e)
                        marked_nodes.add(n)
                        stack.append(n)
                        i = i + 1
                neighbors.clear()
                
            return DFS_iTree
        
        
        def contain_cycle(self,s):
                        
            """ Método que aplica DFS a un grafo para verificar si hay ciclos en él 
                    
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
                if node in(marked_nodes):
                    cycle = True
                else:
                    neighbors = self.neighbors(node)
                    for n in neighbors:
                        if n not in(marked_nodes):
                            stack.append(n)

                neighbors.clear()
                marked_nodes.append(node)
            return cycle
            
        def graph_connected(self):

            """ Método que aplica BFS algorithm al grafo seleccionado para verificar si es no conexo
                    
                    Entrada:
                    
                    Salida:
                        connected = (True or False)
            """
    
            q = queue.Queue()
            
            marked_nodes = set()
            neighbors = []
            
            q.put(0)
            marked_nodes.add(0)

            k=1
            while not q.empty():
                node = q.get()
                
                neighbors = self.neighbors(node)
                for n in neighbors:
                    if n not in(marked_nodes):
                        marked_nodes.add(n)
                        q.put(n)
                        k = k + 1
                neighbors.clear()
            connected = True
            if len(marked_nodes) != len(self.nodes):
                connected = False
            return connected

        
        def Kruskal_D(self,name):
            """ Método para aplicar algoritmo directo de Kruskal a grafo
            
                Entrada:
                    name : Imprimir el nombre del algoritmo  y numero de nodos en consola
                Salida:
                    total : (Impreso en consola) Peso total del árbol
                    MST: Minimun Spanning Tree inducido por el Kruskal Directo 
            """
            
            M = Graph()
            
            #Ordenar aristas de forma ascendente de acuerdo a su peso
            self.edges.sort(key=lambda value: value.weight)
            
            i=0
            total = 0
            #Verificar arista por arista en orden ascendente con respecto a su peso
            for edge in self.edges:
                
                #Verificar si el arista que se dese agregar generaría un ciclo                
                M.edges.append(edge)
                cycle = M.contain_cycle(edge.start)
                M.edges.pop()
                
                # Se agrega en caso que no genere un ciclo
                if cycle == False:
                    M.addEdge(i,edge.start,edge.end,edge.weight)
                    total = total + edge.weight
                    i=i+1
            print(f"{name} Total weight = {round(total,2)}")
            return M
            
        def Kruskal_I(self, name):
            """ Método para aplicar algoritmo directo de Kruskal a grafo
            
                Entrada: 
                    name : Imprimir el nombre del algoritmo  y numero de nodos en consola
                Salida:
                    total : (Impreso en consola) Peso total del árbol
                    MST: Minimun Spanning Tree inducido por el Kruskal Directo 
            """
            
            M = Graph()
            
            #Ordenar aristas de forma descendente de acuerdo a su peso
            self.edges.sort(key=lambda value: value.weight, reverse=True)

            i=0
            total=0
            #Verificar arista por arista en orden descendente con respecto a su peso
            for i in range(len(self.edges)):
                
                #Verificar si el arista que se desea quitar desconectaría el grafo
                edge = self.edges.pop(0)
                connected = self.graph_connected()

                # Se agrega en caso que desconecte el grafo
                if connected != True:
                    self.edges.append(edge)
                    total = total + edge.weight
                    i=i+1
            print(f"{name} Total weight = {round(total,2)}")
            return self
            
        def Prim(self,name):
            """ Método para aplicar el algoritmo de Prim al grafo
            
            Entrada:
                name : Imprimir el nombre del algoritmo  y numero de nodos en consola

            Salida:
                    total : (Impreso en consola) Peso total del árbol
                    MST: Minimun Spanning Tree inducido por el Kruskal Directo
            """
            
            MST = Graph()
            MST.addNode(0)

            visited = set()
            visited.add(0)

            edges_heap = []
            
            #Todos los aristas vecinos del nodo 0 al heap
            for edge in self.edges:
                if edge.start == 0 or edge.end == 0:
                    heapq.heappush(edges_heap, (edge.weight, edge))
            
            total = 0
            
            # Loop de recorrido a todos los aristas del heap
            while edges_heap and len(visited) < len(self.nodes):
            
                # Se extrae el arista con mínimo peso del heap
                weight, edge = heapq.heappop(edges_heap)
                
                # Si nodo inicio o nodo final del arista ya fue visitado se va al siguiente
                if edge.start in visited and edge.end in visited:
                    continue
                    
                # En caso que no, se agrega el arista
                MST.addEdge(edge.id, edge.start, edge.end, edge.weight)
                total = total + edge.weight
                
                # Se escoge uno de los dos nodos
                new_node = edge.end if edge.start in visited else edge.start
                visited.add(new_node)
                
                #Todos los aristas vecinos del nodo al heap
                for next_edge in self.edges:
                    if next_edge.start == new_node and next_edge.end not in visited:
                        heapq.heappush(edges_heap, (next_edge.weight, next_edge))
                    elif next_edge.end == new_node and next_edge.start not in visited:
                        heapq.heappush(edges_heap, (next_edge.weight, next_edge))
                        
            print(f"{name} Total weight = {round(total,2)}")
            return MST
            
