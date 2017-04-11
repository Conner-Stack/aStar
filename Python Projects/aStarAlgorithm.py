import pygame
import math
import graph
import drawablenode
from graph import Graph
from graph import Node

class pathFinder(object):
    
                   Start = [posx , posy]
           Openqueue = []
           Closequeue = []
           Openqueue.append(Start)
           
        def aStart(Start, Goal, graph):

        #the append and insert functions for lists will be how I add to my queue
        #remove will be a function i use to dequeue my nodes        