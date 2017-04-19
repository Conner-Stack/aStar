import pygame
import Astar
from Astar import Node
class Graph(object):
    ''' node graph '''

    def __init__(self, dims):
        '''our graph constructor'''
        col = dims[0]
        row = dims[1]
        self.nodelist = []
        for i in range(0, col):
            for j in range(0, row):
                nodeid = str(i) + str(j)
                
    def getnode(self, node):
        '''gets a node in the graph at value of [1,1]'''
        for i in self.nodelist:
            for j in self.nodelist:
                if node.nodeid is self.nodelist.nodeid:
                    return node

def getNeighbors(node, graph):
    '''gets the node value of neighbors to your current node'''
    right = [1, 0]
    left = [-1, 0]
    top = [0, 1]
    bottom = [0, -1]
    topright = [1, 1]
    bottomright = [1, -1]
    topleft = [-1, 1]
    bottomleft = [-1, -1]
    neighbors = []
    childnodes = [right, left, top, bottom, topleft, topright, bottomleft, bottomright]
    for i in childnodes:
        item1 = i[0] + node.value[0]
        item2 = i[1] + node.value[1]
        grab_node = graph.getNode([item1, item2])
        if grab_node:
            neighbors.append(grab_node)
    return neighbors