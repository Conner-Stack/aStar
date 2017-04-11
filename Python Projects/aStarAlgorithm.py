import pygame
import math
import graph
import drawablenode
from graph import Graph
from graph import Node

class pathFinder(object):
    
    def aStar(start, end):
       start = graph.Node.value
        Openqueue = [start]
        #the append and insert functions for lists will be how I add to my queue
        #remove will be a function i use to dequeue my nodes
        
        