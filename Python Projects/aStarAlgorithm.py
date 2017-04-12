import pygame
import math
import graph
import drawablenode
from graph import Graph
from graph import Node

class pathFinder(object):
    '''pathfinder'''

 
    
#create function to set your start and end goal
    def aStart(Start, Goal, graph):
          
            # create a list to store children
            Open = []
            #create a list to store parents
            Close = []
            #place Start in the open queue
            Open.append(Start)
            current = Start
              for Node in Open:
              if current.value < Node.value:
                      


                    
                      


        #the append and insert functions for lists will be how I add to my queue
        #remove will be a function i use to dequeue my nodes        