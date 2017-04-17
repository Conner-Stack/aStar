import pygame
import math
import graph
import drawablenode
from graph import Graph
from graph import Node
from drawablenode import DrawableNode
from graph import get_neighbors
class pathFinder(object):
    "Pathfinding"

        #create function to set your start and end goal
    def aStar(Start, Goal, graph):
            # create a list to store children
        Openlist = []
            #create a list to store parents
        Closelist = []
            #make a list for children and fill with nodes adjacent to starting node
        fCost = 0
        gScore = 0
        hScore = 0
        #place Start in the open list 
        Openlist.append(Start)
        # while Openlist is not empty do stuff
        while len(Openlist) > 0:
            # lowestindex equals value at Openlist index 0
            lowest = Openlist[0]
            # should state for x as a variable in Openlist
            for x in Openlist:
                # if the fCost of the iterated list item is less than the fCost of variable lowest, lowest equals that list item (x)
                if  Openlist[x].fCost < Openlist[lowest].fCost:
                    lowest = x
                    #moving variable lowest from openlist to closed list (don't know how it even became part of the open list)
                    Openlist.remove(lowest)
                    Closelist.append(lowest)
                    adjacent = graph.get_neighbors(Start)
                    for i in adjacent:
                        
                    
