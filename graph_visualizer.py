import pygame
from pygame.locals import *
from graph import Graph
import random
import math
import numpy

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
    
    def spring_method(self, graph):
        WIDTH, HEIGHT = 1280, 720
        NODE_RADIUS = 10
        k_attraction = 10  # Constante para fuerzas de atracción
        k_repulsion = 5000  # Constante para fuerzas de repulsión
        damping = 0.99  # Factor de amortiguación
        ideal_length = 10 # Longitud ideal de las aristas
        clock = pygame.time.Clock()
        
        nodes = {i: [random.randint(100, 700), random.randint(100, 500)] for i in range(len(graph.nodes))}
        
        edges = []
        for edge in graph.edges:
            e = (edge.start, edge.end)
            edges.append(e)
        
        forces = {i: [0, 0] for i in range(len(graph.nodes))}

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            
            if True:# k<100:
                forces = {i: [0, 0] for i in range(len(graph.nodes))}

                # Fuerzas de repulsión
                for i in nodes:
                    for j in nodes:
                        if i != j:
                            dx = nodes[i][0] - nodes[j][0]
                            dy = nodes[i][1] - nodes[j][1]
                            dist = max(self.distance(nodes[i], nodes[j]), ideal_length)
                            force = k_repulsion / dist**2
                            forces[i][0] += force * dx / dist
                            forces[i][1] += force * dy / dist
                # Fuerzas de atracción (logarítmicas)
                for edge in edges:
                    i , j = edge
                    dx = nodes[j][0] - nodes[i][0]
                    dy = nodes[j][1] - nodes[i][1]
                    dist = max(self.distance(nodes[i], nodes[j]), ideal_length)
                    force = k_attraction * math.log10(dist / ideal_length)
                    forces[i][0] += force * dx / dist
                    forces[i][1] += force * dy / dist
                    forces[j][0] -= force * dx / dist
                    forces[j][1] -= force * dy / dist

                # Actualizar posiciones de los nodos
                for i in nodes:
                    nodes[i][0] += forces[i][0] * damping
                    nodes[i][1] += forces[i][1] * damping
                    nodes[i][0] = max(NODE_RADIUS, min(WIDTH - NODE_RADIUS, nodes[i][0]))
                    nodes[i][1] = max(NODE_RADIUS, min(HEIGHT - NODE_RADIUS, nodes[i][1]))
            
            self._display_surf.fill((250,236,255))
            
            for edge in edges:
                pygame.draw.line(self._display_surf, (100, 100, 100), nodes[edge[0]], nodes[edge[1]], 1)
            for i in nodes:
                pygame.draw.circle(self._display_surf, (8,54,159), (int(nodes[i][0]), int(nodes[i][1])), NODE_RADIUS)
        
            pygame.display.flip()
            clock.tick(60)
            #draw a straight-line segment for each edge

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self,graph):
        if self.on_init() == False:
            self._running = False

        #while (self._running):
        #    for event in pygame.event.get():
        #        self.on_event(event)
        #    self.on_loop()
        self.spring_method(graph)
        #    pygame.display.update()
        self.on_cleanup()


#if __name__ == "__main__":
 #   graph = App()
  #   graph.on_execute()
