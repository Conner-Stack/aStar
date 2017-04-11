import pygame
import math
import graph
import drawablenode
from graph import Graph
from graph import Node

class pathFinder(object):
    '''pathfinder'''

 
    

    def aStart(Start, Goal, graph):
            Openqueue = []
            Closequeue = []
            Openqueue.append(Start)
            current = Start
            Openqueue.append(current)  
            while current!=Goal:
                #make current equal a child node
                current = 
                Closequeue.append(current)

                    
                      


        #the append and insert functions for lists will be how I add to my queue
        #remove will be a function i use to dequeue my nodes        