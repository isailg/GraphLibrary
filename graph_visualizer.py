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
        c1=2
        c2=1
        c3=1
        c4=0.1
        #Initialize Positions
        list_pos = []
        for node in graph.nodes:
            pos = numpy.array([random.randint(30,1250),random.randint(30,690)])
            list_pos.append(pos)
        self._display_surf.fill('white')

        for pos in list_pos:
            pygame.draw.circle(self._display_surf, (255,100,255),pos, 9)
        pygame.display.flip()

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            i=0
            fa,fr = 0,0
            for node in graph.nodes:
                print(list_pos[i][0],list_pos[i][1])                
                #Attractive Forces
                neighbors = graph.neighbors(node.id)
                print(neighbors)
                for m in neighbors:
                    d = max(self.distance(list_pos[i],list_pos[m]),1)
                    if d!=0:
                        fa = c1*math.log10(d/c2)
                        dx = list_pos[i][0]-list_pos[m][0]
                        dy = list_pos[i][1]-list_pos[m][1]
                        list_pos[i][0] = list_pos[i][0] + c4*fa*dx/d
                        list_pos[i][1] = list_pos[i][1] + c4*fa*dy/d
                    
                #Repulsive Forces
                for n in list_pos:
                    d = max(self.distance(list_pos[i],n),1)
                    if d != 0:
                        fr = c3/math.sqrt(d)
                        dx = list_pos[i][0]-n[0]
                        dy = list_pos[i][1]-n[1]
                        #list_pos[i][0] = list_pos[i][0] + c4*fr*dx/d
                        #list_pos[i][1] = list_pos[i][1] + c4*fr*dy/d

                        
                #calculate the force acting on each vertex
                #move the vertex c4*(force on vertex)
                print(list_pos[i][0],list_pos[i][1])

                #list_pos[i][0] = list_pos[i][0] + int(c4*(fax))*
                
                #print(fax,fay)
                #list_posx[i] = #c4*(fax-frx)
                #list_posy[i] =+ 30 #c4*(fay-fry)
                i=i+1
            
            self._display_surf.fill('white')

            for edge in graph.edges:
                pygame.draw.line(self._display_surf, (200,200,200),list_pos[edge.start], list_pos[edge.end],1)

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
