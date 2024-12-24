import pygame
from pygame.locals import *
from graph import Graph
import random
import math

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
    
    def spring_method(self, graph):
        clock = pygame.time.Clock()
        c1=2
        c2=50
        c3=1
        c4=10
        #Initialize Positions
        list_posx = []
        list_posy = []
        for node in graph.nodes:
            posx = random.randint(30,1250)
            list_posx.append(posx)
            posy = random.randint(30,690)
            list_posy.append(posy)
        self._display_surf.fill('white')
        fax, fay = 0,0
        frx,fry = 0,0

        k=0
        for pos in list_posx:
            pygame.draw.circle(self._display_surf, (255,100,255),(pos,list_posy[k]), 9)
            k=k+1
        pygame.display.flip()

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            i=0
            for node in graph.nodes:

                #Atraction Forces
                neighbors = graph.neighbors(node)
                for m in neighbors:
                    d = abs(list_posx[i] - list_posx[m])
                    fax = fax + c1*math.log10(d/c2)
                    d = abs(list_posx[i] - list_posx[m])
                    fay = fay + c1*math.log10(d/c2)

                #Repulsion Forces
                for n in list_posx:
                    d = abs(list_posx[i]-n)
                    if d != 0:
                        frx = frx + c3/(d*d)
                for n in list_posy:
                    d = abs(list_posy[i]-n)
                    if d != 0:
                        fry = fry + c3/(d*d)
                #calculate the force acting on each vertex
                #move the vertex c4*(force on vertex)
                list_posx[i] =+ 30 #c4*(fax-frx)
                list_posy[i] =+ 30 #c4*(fay-fry)
                i=i+1
            
            self._display_surf.fill('white')

            #draw a filled circle for each vertex
            k=0
            for pos in list_posx:
                pygame.draw.circle(self._display_surf,(255,100,255) ,(pos,list_posy[k]), 9)
                k=k+1
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
