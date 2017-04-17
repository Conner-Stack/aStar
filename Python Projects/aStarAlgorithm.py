import pygame
import math
import graph
import drawablenode
from graph import Graph
from graph import Node
from drawablenode import DrawableNode
class pathFinder(object):
    '''pathfinder'''  
    #create function to set your start and end goal
    def aStart(self, Start, Goal):
            # create a list to store children
        Openlist = []
            #create a list to store parents
        Closelist = []
            #make a list for children
        Children = []
        fCost = 0
        gScore = 0
        hScore = 0
        #place Start in the open list 
        Openlist.append(Start)
        while len(Openlist) > 0:
            lowest = Openlist[0]
            for x in Openlist:
                if  x.fCost < lowest.fCost:
                    lowest = x
                    Openlist.remove(lowest)
                    Closelist.append(lowest)
