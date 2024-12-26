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
        clock = pygame.time.Clock()
        c1=2 #attraction
        c2=1 #lenght
        c3=1 #repulsion
        c4=0.1 
        
        #Initialize Positions
        list_pos = []
        for node in graph.nodes:
            pos = numpy.array([random.randint(30,1250),random.randint(30,690)])
            list_pos.append(pos)
        self._display_surf.fill('white')

        for pos in list_pos:
            pygame.draw.circle(self._display_surf, (66,66,66),pos, 9)
        pygame.display.flip()

        forces = numpy.zeros((len(graph.nodes),2))

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            
            fa,fr = 0,0

            print(forces)
            """
            #Repulsive forces
            for i in range(len(graph.nodes)):
                for j in range (len(graph.nodes)):
                    if i!=j:
                        dx = list_pos[i][0] - list_pos[j][0]
                        dy = list_pos[i][1] - list_pos[j][1]
                        d = max(self.distance(list_pos[i], list_pos[j]),1)
                        if d != 0:
                            force = c3/d**2
                            forces[i][0] = forces[i][0] + force * dx/d
                            forces[i][1] = forces[i][1] + force * dy/d
            """
            #Attractive forces
            for edge in graph.edges:
                dx = list_pos[edge.start][0] - list_pos[edge.end][0]
                dy = list_pos[edge.start][1] - list_pos[edge.end][1]
                d = max(self.distance(list_pos[edge.start], list_pos[edge.end]),1)
                force = c1*math.log10(d/c2)
                forces[edge.start][0] = forces[edge.start][0] + force*dx/d
                forces[edge.start][1] = forces[edge.start][1] + force*dy/d
                forces[edge.end][0] = forces[edge.end][0] - force*dx/d
                forces[edge.end][1] = forces[edge.end][1] - force*dy/d
            
            """
            for node in graph.nodes:
                print(list_pos[i][0],list_pos[i][1])                
                #Attractive Forces
                neighbors = graph.neighbors(node.id)
                print(neighbors)
                forces = numpy.array([[0,0],[0,0]])
                for edge in graph.edges:
                    d = max(self.distance(list_pos[edge.start],list_pos[edge.end]),1)
                    if d!=0:
                        fa = c1*math.log10(d/c2)
                        dx = list_pos[edge.start][0]-list_pos[edge.end][0]
                        dy = list_pos[edge.start][1]-list_pos[edge.end][1]
                        forces[1][0] = forces[0] + c4*fa*dx/d
                        forces[1][1] = forces[1] + c4*fa*dy/d
            """
            #Repulsive Forces
            """
                for n in list_pos:
                    d = max(self.distance(list_pos[i],n),1)
                    if d != 0:
                        fr = c3/math.sqrt(d)
                        dx = list_pos[i][0]-n[0]
                        dy = list_pos[i][1]-n[1]
                        forces = list_pos[i][0] + c4*fr*dx/d
                        #list_pos[i][1] = list_pos[i][1] + c4*fr*dy/d
            """     
            #calculate the force acting on each vertex
            #move the vertex c4*(force on vertex)
            print(forces)
            print(list_pos)
            
            for i in range(len(list_pos)):
                list_pos[i][0] = list_pos[i][0] + forces[i][0]*c4
                list_pos[i][1] = list_pos[i][1] + forces[i][1]*c4
                list_pos[i][0] = max(10, min(1280-10,list_pos[i][0]))
                list_pos[i][1] = max(10, min(720 - 10, list_pos[i][1]))
                
                print(list_pos[i][0],list_pos[i][1])

                #list_pos[i][0] = list_pos[i][0] + int(c4*(fax))*
                
                #print(fax,fay)
                #list_posx[i] = #c4*(fax-frx)
                #list_posy[i] =+ 30 #c4*(fay-fry)
            
            self._display_surf.fill('white')

            for edge in graph.edges:
                pygame.draw.line(self._display_surf, (200,200,200),list_pos[edge.start],list_pos[edge.end],1)

            #draw a filled circle for each vertex
            for pos in list_pos:
                pygame.draw.circle(self._display_surf,(66,66,66) ,pos, 9)

            pygame.display.update()
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
