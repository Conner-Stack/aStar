import pygame
import math
import newgraph
from newgraph import Graph
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
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0

    def empty(self, queue):
        '''returns a bool with value of true if list is empty'''
        if queue is 0:
            return True

    def hvalue(self, goalnode):
        '''for calculating h'''
        self.hscore = 10 * (abs(self.posx - goalnode.posx) + abs(self.posy - goalnode.posy))
        return self.hscore

    def fcost(self):
        '''finishes the equation'''
        self.fscore = self.gscore + self.hscore
        return self.fscore

def gvalue(currentnode, neighbor):
    '''for calculating g'''

def astar(start, goal, graph):
    '''this is our pathfinder, hopefully'''
    openlist = []
    closelist = []
    Openlist.append(start)
    while empty(Openlist) is False:
        for i in Openlist:
            if i.walkable is False or i in Closelist:
                continue
            else:
                Current = Openlist[0]
