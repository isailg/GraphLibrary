import pygame
from pygame.locals import *
from graph import Graph
import random
import math
import numpy
import cv2


class Quadtree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary  # (x_min, x_max, y_min, y_max)
        self.capacity = capacity
        self.nodes = []
        self.divided = False
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

    def subdivide(self):
        x_min, x_max, y_min, y_max = self.boundary
        mid_x = (x_min + x_max) / 2
        mid_y = (y_min + y_max) / 2

        nw = (x_min, mid_x, y_min, mid_y)
        ne = (mid_x, x_max, y_min, mid_y)
        sw = (x_min, mid_x, mid_y, y_max)
        se = (mid_x, x_max, mid_y, y_max)

        self.nw = Quadtree(nw)
        self.ne = Quadtree(ne)
        self.sw = Quadtree(sw)
        self.se = Quadtree(se)

        self.divided = True

    def insert(self, node):
        x, y = node
        x_min, x_max, y_min, y_max = self.boundary
        if not (x_min <= x <= x_max and y_min <= y <= y_max):
            return False
        
        if len(self.nodes) < self.capacity:
            self.nodes.append(node)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.nw.insert(node): return True
            if self.ne.insert(node): return True
            if self.sw.insert(node): return True
            if self.se.insert(node): return True

        return False

    def query(self, range, threshold):
        found_nodes = []
        x_min, x_max, y_min, y_max = self.boundary
        rx_min, rx_max, ry_min, ry_max = range
        if x_max < rx_min or x_min > rx_max or y_max < ry_min or y_min > ry_max:
            return found_nodes
        
        # Si el quadtree ha sido subdividido, se busca recursivamente
        if self.divided:
            found_nodes.extend(self.nw.query(range, threshold))
            found_nodes.extend(self.ne.query(range, threshold))
            found_nodes.extend(self.sw.query(range, threshold))
            found_nodes.extend(self.se.query(range, threshold))
        else:
            for node in self.nodes:
                if self.distance(range, node) < threshold:
                    found_nodes.append(node)

        return found_nodes

    def distance(self, range, node):
        rx_min, rx_max, ry_min, ry_max = range
        return math.sqrt((node[0] - rx_min) ** 2 + (node[1] - ry_min) ** 2)

    def draw(self, surface, color=(0, 0, 0)):
        
        x_min, x_max, y_min, y_max = self.boundary
        pygame.draw.rect(surface, color, pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min), 1)
        
        if self.divided:
            self.nw.draw(surface, color)
            self.ne.draw(surface, color)
            self.sw.draw(surface, color)
            self.se.draw(surface, color)