import pygame
import math

class Graph(object):
    ''' node graph '''

    def __init__(self, dims):
        '''our graph constructor'''
        col = dims[0]
        row = dims[1]
        self.nodeList = []
        for i in range(0, col):
            for j in range(0, row):
                self.nodeList.append(str(i) + ',' + str(j))

    def getNode(self, id):
        '''gets a node in the graph'''
        for i in self.nodeList:
            if i.id is id:
                return i
        return None

def getNeighbors(node, graph):
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