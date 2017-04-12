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
    def aStart(Start, Goal, graph):
          
            # create a list to store children
            Open = []
            #create a list to store parents
            Close = []
            Start = DrawableNode
            Start.f = 0
            #place Start in the open queue
            Open.append(Start)
            current = Start
            node = DrawableNode
              for node in Open:
                  #not right, but kind of a placeholder until i figure out how to do it
              if current.value < node.f:
                  
                  