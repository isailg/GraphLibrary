import pygame
from pygame.locals import *
from graph import Graph
import random
import math
import numpy
import cv2

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 720

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Graph Visualization')
        clock = pygame.time.Clock()
        self._running = True
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def distance(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    
    def spring_method(self, graph, name):
        #Declaración de constantes
        width, height = 1280, 720
        vertex_size = 10
        c1 = 1
        c2 = 25
        c3 = 2
        c4 = 0.99

        clock = pygame.time.Clock()
        
        #OpenCV para grabar video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 60
        out = cv2.VideoWriter(name+".mp4", fourcc, fps, (width, height))
        
        #Conversión de nodos y aristas del grafo a listas
        nodes = {i: [random.randint(100, 1250), random.randint(100, 690)] for i in range(len(graph.nodes))}
        edges = []
        for edge in graph.edges:
            e = (edge.start, edge.end)
            edges.append(e)
        
        f = {i: [0, 0] for i in range(len(graph.nodes))}
        
        #Loop principal
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
                
            # Paso del método Spring
            if True: #if(k<100): NOTA: Se pretendía usar solo 100iteraciones pero mejor sin limite
                
                #Lista de fuerzas calculadas, se reinicia en ceros en cada iteración
                f = {i: [0, 0] for i in range(len(graph.nodes))}

                #Fuerzas de repulsión
                for i in nodes:
                    for j in nodes:
                        if i != j:
                            dx = nodes[i][0] - nodes[j][0]
                            dy = nodes[i][1] - nodes[j][1]
                            d = max(self.distance(nodes[i], nodes[j]), c2)
                            force = c3 / math.sqrt(d)
                            f[i][0] += force * dx / d
                            f[i][1] += force * dy / d
                
                #Fuerzas de atracción
                for edge in edges:
                    i , j = edge
                    dx = nodes[j][0] - nodes[i][0]
                    dy = nodes[j][1] - nodes[i][1]
                    d = max(self.distance(nodes[i], nodes[j]), c2)
                    force = c1 * math.log10(d / c2)
                    f[i][0] += force * dx / d
                    f[i][1] += force * dy / d
                    f[j][0] -= force * dx / d
                    f[j][1] -= force * dy / d

                #Actualización de posiciones de cada nodo
                for i in nodes:
                    nodes[i][0] += f[i][0] * c4
                    nodes[i][1] += f[i][1] * c4
                    nodes[i][0] = max(vertex_size, min(width - vertex_size, nodes[i][0]))
                    nodes[i][1] = max(vertex_size, min(height - vertex_size, nodes[i][1]))
            
            #Se limpia la pantalla
            self._display_surf.fill((250,236,255))
            
            #Se dibujan aristas en sus nuevas posiciones
            for edge in edges:
                pygame.draw.line(self._display_surf, (100, 100, 100), nodes[edge[0]], nodes[edge[1]], 1)
            
            #Se dibujan nodos en sus nuevas posiciones
            for i in nodes:
                pygame.draw.circle(self._display_surf, (8,54,159), (int(nodes[i][0]), int(nodes[i][1])), vertex_size)
            
            #Conversión del pygame frame a OpenCV frame
            frame = pygame.surfarray.array3d(self._display_surf)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = cv2.transpose(frame)
            out.write(frame)
            
            pygame.display.flip()
            clock.tick(60)
            
        #Se guarda el video OpenCV
        out.release()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self,graph, name):
        if self.on_init() == False:
            self._running = False
        
        self.spring_method(graph, name)
        
        self.on_cleanup()
