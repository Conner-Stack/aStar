import pygame
import math
import newgraph
from newgraph import Graph as graph
from newgraph import getNeighbors

class Node(object):
    '''class for Nodes'''

    def __init__(self, position):
        '''this is the init'''
        self.adjacent = []
        self.posx = position[0]
        self.posy = position[1]
        self.parent = None
        self.walkable = True
        self.gScore = 0
        self.hScore = 0
        self.fScore = 0

    def empty(self, queue):
        '''returns a bool with value of true if list is empty'''
        if queue is 0:
            return True

    def hValue(self, currentNode, goalNode):
        '''for calculating h'''
        h = 10 * (abs(currentNode.posx - goalNode.posx) + abs(currentNode.posy - goalNode.posy))
        return h
        #function for getting the value of g
    def gValue(self, currentnode):
        '''for calculating g'''
        #makes childnodes a list of the neighbors of the currentnode
        childnodes = currentnode.getNeightbors
        #for each element iterated in childnodes
        for i in childnodes:
            dirr = [i[0] - currentnode[0], i[1] - currentnode[1]]
            if  dirr in currentnode.neighbors.diag:
                score = currentnode.gValue(parent) + 14
                return score

    def fCost(currentNode, goalNode):
        g = gValue(currentNode)
        h = hValue(currentNode, goalNode)
        f = g + h
        return f
def aStar(start, goal, graph):
    '''this is our pathfinder, hopefully'''
    Openlist = []
    Closelist = []
    Openlist.append(start)
    while empty(Openlist) is False:
        for i in Openlist:
            if i.walkable is False or i in Closelist:
                continue
            else:
                Current = Openlist[0]
