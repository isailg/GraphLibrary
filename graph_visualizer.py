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

    def fr(self,k,x):
        return (k**2)/x
    
    def fa(self,k,x):
        return (x**2) / k
    
    def distance(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        
    def norma(self,dx,dy):
        return math.sqrt((dx**2)+(dy**2))
        
    def strength(self,p0,p1):
        return 1/min(graph.getDegree(p0),graph.getDegree(p1))
    
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
    
    def fruchterman_reingold_method(self, graph, name):
        #Declaración de constantes
        W, L = 1280, 720
        vertex_size = 10
        k = 200
        t= W/10#0.95
        a= 20
        
        area = W*L
        
        
        #OpenCV para grabar video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 60
        out = cv2.VideoWriter(name+".mp4", fourcc, fps, (W, L))
        clock = pygame.time.Clock()
        
        #Place vertices at random
        nodes = {i: [random.randint(600, W-600), random.randint(300, L-300)] for i in range(len(graph.nodes))}
        
        # Compute optimal pairwase distance
        #k = math.sqrt(area/(len(nodes)))
        
        # Conversión aristas del grafo a listas
        edges = []
        for edge in graph.edges:
            e = (edge.start, edge.end)
            edges.append(e)
        
        # Main Loop
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            
            f = {i: [0, 0] for i in range(len(graph.nodes))}
            
            # Compute repulsive forces
            for v in nodes:
                #Se inicializa vector de desplazamientos
                f[v] = [0,0]
                for u in nodes:
                    if (v!=u):
                        dx = nodes[v][0] - nodes[u][0]
                        dy = nodes[v][1] - nodes[u][1]
                        d = self.norma(dx,dy)
                        if d > 0:
                            f[v][0] += (dx / d) * self.fr(k,d)
                            f[v][1] += (dy / d) * self.fr(k,d)
            # Compute atrattive forces
            for e in edges:
                dx = nodes[e[1]][0] - nodes[e[0]][0]
                dy = nodes[e[1]][1] - nodes[e[0]][1]
                d = self.norma(dx,dy)
                if d > 0:
                    f[e[1]][0] = f[e[1]][0] - (dx/d)*self.fa(k,d)
                    f[e[1]][1] = f[e[1]][1] - (dy/d)*self.fa(k,d)
                    f[e[0]][0] = f[e[0]][0] + (dx/d)*self.fa(k,d)
                    f[e[0]][1] = f[e[0]][1] + (dy/d)*self.fa(k,d)
            difx,dify = 0,0
            for v in nodes:
                # limit max displacement to frame; use temp. t to scale
                
                norf = self.norma(f[v][0],f[v][1])
                if norf > 0:
                    nodes[v][0] = nodes[v][0] + (f[v][0]/norf)
                    nodes[v][1] = nodes[v][1] + (f[v][1]/norf)
                    #nodes[v][0] = min(W/2,max(-W/2,nodes[v][0]))
                    #nodes[v][1] = min(L/2,max(-L/2,nodes[v][1]))
                nodes[v][0] = max(vertex_size, min(W - vertex_size, nodes[v][0]))
                nodes[v][1] = max(vertex_size, min(L - vertex_size, nodes[v][1]))
                
                
            #Reduce temperature for next iteration
            if t < 1:
                continue
            t = t - 0.001
            
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
    
    def barnes_hut_method(self, graph, name):
        #Initial parameter
        W, L = 1280, 720
        vertex_size = 10
        D = 20
        Iterations_number=
        alpha =
        alphaMin=
        alphaDecay = 1 - alphaMin**(1/Iterations_number)
        
        
        #Create Quadtree
        
        
        #OpenCV para grabar video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 60
        out = cv2.VideoWriter(name+".mp4", fourcc, fps, (W, L))
        clock = pygame.time.Clock()
        
        
        
        
        #Place vertices at random
        nodes = {i: [random.randint(600, W-600), random.randint(300, L-300)] for i in range(len(graph.nodes))}
        
        # Conversión aristas del grafo a listas
        edges = []
        for edge in graph.edges:
            e = (edge.start, edge.end)
            edges.append(e)
            
            
            
        # Main Loop
        while (self._running) and alpha < alphaMin:
        
            for event in pygame.event.get():
                self.on_event(event)
                
            #Inicia vector de desplazamientos
            desp = {i: [0, 0] for i in range(len(graph.nodes))}
            
            for v in nodes:
                
                #Calculate elasticity from adjacent nodes
                neighbors = graph.neighbors(v)
                for u in neighbors:
                    dist = self.distance(nodes[v],nodes[u])
                    f_spr = (dist - D)*strength(v,u)
                    dx = nodes[v][0] - nodes[u][0]
                    dy = nodes[v][1] - nodes[u][1]
                        if dist > 0:
                            desp[v][0] += (dx / dist) * f_spr
                            desp[v][1] += (dy / dist) * f_spr
                            
                #Barnes-Hut approximate
                
                #Calculate repulsion from any other nodes by quadtree
                
                
                #Calculate resultant force
                
                #Velocity Increment
                
                #System temperature decay
                
                #Update nodes velocity
                
                #Displacement increment
                
                #Update nodes position
                
            #Update quadtree
            
            
                #Se inicializa vector de desplazamientos
                f[v] = [0,0]
                for u in nodes:
                    if (v!=u):
                        dx = nodes[v][0] - nodes[u][0]
                        dy = nodes[v][1] - nodes[u][1]
                        d = self.norma(dx,dy)
                        if d > 0:
                            f[v][0] += (dx / d) * self.fr(k,d)
                            f[v][1] += (dy / d) * self.fr(k,d)
            # Compute atrattive forces
            for e in edges:
                dx = nodes[e[1]][0] - nodes[e[0]][0]
                dy = nodes[e[1]][1] - nodes[e[0]][1]
                d = self.norma(dx,dy)
                if d > 0:
                    f[e[1]][0] = f[e[1]][0] - (dx/d)*self.fa(k,d)
                    f[e[1]][1] = f[e[1]][1] - (dy/d)*self.fa(k,d)
                    f[e[0]][0] = f[e[0]][0] + (dx/d)*self.fa(k,d)
                    f[e[0]][1] = f[e[0]][1] + (dy/d)*self.fa(k,d)
            difx,dify = 0,0
            for v in nodes:
                # limit max displacement to frame; use temp. t to scale
                
                norf = self.norma(f[v][0],f[v][1])
                if norf > 0:
                    nodes[v][0] = nodes[v][0] + (f[v][0]/norf)
                    nodes[v][1] = nodes[v][1] + (f[v][1]/norf)
                    #nodes[v][0] = min(W/2,max(-W/2,nodes[v][0]))
                    #nodes[v][1] = min(L/2,max(-L/2,nodes[v][1]))
                nodes[v][0] = max(vertex_size, min(W - vertex_size, nodes[v][0]))
                nodes[v][1] = max(vertex_size, min(L - vertex_size, nodes[v][1]))
                
                
            #Reduce temperature for next iteration
            if t < 1:
                continue
            t = t - 0.001
            
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
        
        self.fruchterman_reingold_method(graph, name)
        
        self.on_cleanup()
        
    def fruchterman_reingold(self,graph, name):
        if self.on_init() == False:
            self._running = False
        
        self.fruchterman_reingold_method(graph, name)
        
        self.on_cleanup()
        
    def on_execute(self,graph, name):
        if self.on_init() == False:
            self._running = False
        
        self.fruchterman_reingold_method(graph, name)
        
        self.on_cleanup()

