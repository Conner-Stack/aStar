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

    def hvalue(self, currentnode, goalnode):
        '''for calculating h'''
        currentnode.hScore = 10 * (abs(currentnode.posx - goalnode.posx) + abs(currentnode.posy - goalnode.posy))
        return hScore
        #function for getting the value of g
    def gvalue(self, currentnode):
        '''for calculating g'''
        #makes childnodes a list of the neighbors of the currentnode
        childnodes = currentnode.getNeightbors
        if currentnode.posx is childnodes.posx or currentnode.posy is childnodes.posy:
            gScore = currentnode.gScore + 10 
        else:
            gScore = currentnode.gScore + 14
        return gScore

    def fCost(currentNode, goalNode):
        f = gValue(currentNode) + hValue(currentNode, goalNode)
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
