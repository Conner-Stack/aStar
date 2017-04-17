import pygame


class Node(object):
    '''class for Nodes'''

    def __init__(self, node):
        '''this is the init'''
        self.adjacent = []
        posx = node.value[0]
        posy = node.value[1]
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
            
        def aStar(start, goal, graph):
            '''this is our pathfinder, hopefully'''
            Openlist = []
            Closelist = []
            Start = []
            Openlist.append(start)
            while empty(Openlist) is False:
                current.node._f = start.node._f


            
                
                
                 
                
            

        
