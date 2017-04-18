import pygame
import math
class Node(object):
    '''class for Nodes'''

    def __init__(self, node):
        '''this is the init'''
        self.adjacent = []
        self.posx = node.value[0]
        self.posy = node.value[1]
        self.parent = None
        self.walkable = True
        self._g = 0
        self._h = 0
        self._f = 0

        @property
        def f(self):
            '''get f'''
            return self._f
        @property
        def g(self):
            '''get g'''
            return self._g
        @property
        def h(self):
            '''get h'''
            return self._h
        @f.setter
        def f(self, value):
            self._f = value
        @g.setter
        def g(self, value):
            self._g = value
            self._f = self._g + self._h
        @h.setter
        def h(self, value):
            self._h = value
            self._f = self._g + self._h

        def empty(queue):
            '''returns a bool with value of true if list is empty'''
            for i in queue:
                return bool(i = None)

        def hValue(currentNode, goalNode):
            '''for calculating h'''
            hValue = 10 * (abs(currentNode.posx - goalNode.posx) + abs(currentNode.posy - goalNode.posy))
            return h
            #function for getting the value of g
        def gValue(currentNode):
            '''for calculating g'''
            #makes childnodes a list of the neighbors of the currentnode
            childnodes = currentNode.neighbors
            score = 0
            #for each element iterated in childnodes
            for i in childnodes:
                if i.walkable is True:
                    dirr = [i[0] - currentNode[0], i[1] - currentNode[1]]
                    if  dirr in currentNode.neighbors.diag:
                        score = currentNode._g + 14

        def neighbors(node):
            right = [1, 0]
            left = [-1, 0]
            top = [0, 1]
            bottom = [0, -1]
            topright = [1, 1]
            bottomright = [1 , -1]
            topleft = [-1 , 1]
            bottomleft = [1, -1]
            neighbors = []
            childnodes = [right, left, top, bottom, topleft, topright, bottomleft, bottomright]
            horiz = [right, left]
            diag = [topleft, topright, bottomleft, bottomright]
            vert = [top, bottom]
            for i in childnodes:
                x = i[0] + node.value[0]
                y = i[1] + node.value[1]
                grab_node = graphnode(x,y)
                if grab_node:
                    neighbors.append(graphnode)
            return neighbors
                            
                        
        def aStar(start, goal, graph):
            '''this is our pathfinder, hopefully'''
            Openlist = []
            Closelist = []
            Start = []
            
            cameFrom[start] = None
            gScore
            Openlist.append(start)
            fScore
            while empty(Openlist) is False:
                for i in Openlist:
                    if i.walkable is False or i in Closelist:
                        continue
                    else:
                        Current = Openlist[0]
