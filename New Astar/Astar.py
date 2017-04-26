'''Astar.py'''
class Node(object):
    '''class for Nodes'''

    def __init__(self, position, identifier):
        '''this is the init'''
        self.adjacent = []
        self.position = position
        self.parent = None
        self.walkable = True
        self.gscore = 0

        self.hscore = 0
        self.fscore = 0
        self.identity = identifier
        self.neighbors = []

    def __str__(self):
        '''overload for printing'''
        return 'posx {0}, posy{1}, identity: {2}'.format(self.position[0],
                                                         self.position[1], self.identity)

    def __getitem__(self, key):
        return self.position[key]


def hvalue(currentnode, goalnode):
    '''for calculating h'''
    hscore = 10 * (abs(currentnode[0] - goalnode[0]) +
                   abs(currentnode[1] - goalnode[1]))
    currentnode.hscore = hscore


def fcost(node):
    '''finishes the equation'''
    fscore = node.gscore + node.hscore
    node.fscore = fscore


def gvalue(currentnode, neighbor):
    '''for calculating g'''
    tentativeg = 0
    if currentnode.position[0] is neighbor.position[0] \
    or currentnode.position[1] is neighbor.position[1]:
        tentativeg = currentnode.gscore + 10
    else:
        tentativeg = currentnode.gscore + 14
    if neighbor.parent is None:
        neighbor.gscore = tentativeg
    else:
        if tentativeg < neighbor.gscore:
            neighbor.parent = currentnode
            neighbor.gscore = tentativeg

def astar(start, goal, graph):
    '''this is our pathfinder, hopefully'''
    openlist = []
    closelist = []
    path = []
    came_from = None
    current = start
    openlist.append(current)
    while openlist is not None:
        openlist.remove(current)
        closelist.append(current)
        current.neighbors = getneighbors(current, graph)
        for node in current.neighbors:
            if node not in closelist:
                openlist.append(node)
                gvalue(current, node)
                hvalue(node, goal)
                fcost(node)
        openlist.sort(key=lambda node: node.fscore)
        came_from = current
        path.append(came_from)
        current = openlist[0]
        return path

class Graph(object):
    ''' node graph '''

    def __init__(self, dims):
        '''our graph constructor'''
        col = dims[0]
        row = dims[1]
        self.nodelist = []
        for i in range(0, col):
            for j in range(0, row):
                nodeid = str(i) + "," + str(j)
                self.nodelist.append(Node([i, j], nodeid))

    def getnode(self, nodeid):
        '''gets a node in the graph at value of [1,1]'''
        return self.nodelist[nodeid]

def getneighbors(node, graph):
    '''gets the node value of neighbors to your current node'''
    right = [1, 0]
    left = [-1, 0]
    top = [0, 1]
    bottom = [0, -1]
    topright = [1, 1]
    bottomright = [1, -1]
    topleft = [-1, 1]
    bottomleft = [-1, -1]
    neighbors = []
    childnodes = [right, left, top, bottom,
                  topleft, topright, bottomleft, bottomright]
    for i in childnodes:
        item1 = i[0] + node.value[0]
        item2 = i[1] + node.value[1]
        grab_node = graph.getNode([item1, item2])
        if grab_node is not None and grab_node.walkable:
            neighbors.append(grab_node)
    return neighbors

#This is a comment

