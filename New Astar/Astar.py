'''Astar.py'''
class Node(object):
    '''class for Nodes'''

    def __init__(self, position, identifier):
        '''this is the init'''
        #sets the position on the graph for the node
        self.position = position
        #sets the parent per node
        self.parent = None
        #sets if the node is walkable or an obstacle
        self.walkable = True
        #sets the gscore for the equation
        self.gscore = 0
        #sets the hscore for the equation
        self.hscore = 0
        #sets the fscore for the equation
        self.fscore = 0
        #sets the id of the node in the graph
        self.identity = identifier
        #sets each neighbor per node
        self.neighbors = []
    #not sure
    #def __str__(self):
       # '''overload for printing'''
        #return 'posx {0}, posy{1}, identity: {2}'.format(self.position[0],
         #                                                self.position[1], self.identity)

    def __getitem__(self, key):
        return self.position[key]


def hvalue(currentnode, goalnode):
    '''for calculating h'''
    #sets hscore to equal the absolute value of the current node
    # coordinates minus the goal node coordinates multiplied by 10
    hscore = 10 * (abs(currentnode[0] - goalnode[0]) +
                   abs(currentnode[1] - goalnode[1]))
    #sets the hscore for the node in the node class
    currentnode.hscore = hscore


def fvalue(node):
    '''finishes the equation'''
    #sets f = g + h equation
    fscore = node.gscore + node.hscore
    node.fscore = fscore


def gvalue(currentnode, neighbor):
    '''for calculating g'''
    #tentative g is used to go back in case there is a better cost
    tentativeg = 0
    #a conditional evaluating one of the coordinates in the same dimension as the neighbor
    if currentnode.position[0] is neighbor.position[0] \
    or currentnode.position[1] is neighbor.position[1]:
        #if evaluation is true, must be horiz or vert so add 10
        tentativeg = currentnode.gscore + 10
    else:
        #else is diagonal, so add 14
        tentativeg = currentnode.gscore + 14
    #if there is no parent for the neighbor, set the gscore for neighbor to the tent. g
    if neighbor.parent is None:
        neighbor.gscore = tentativeg
    else:
        #conditional stating if the tent. g is less that the gscore of the neighbors
        #the parent of the neighbor is the currentnode
        if tentativeg < neighbor.gscore:
            neighbor.parent = currentnode
            #makes the gscore of the neighbor equal to tentative g
            neighbor.gscore = tentativeg


class Graph(object):
    ''' node graph '''

    def __init__(self, dims):
        '''our graph constructor'''
        #col and row is the x y dimensions for the 2D graph
        col = dims[0]
        row = dims[1]
        #lists all the nodes in the graph
        self.nodelist = []
        #loops through col every time the row loop finishes to generate the graph
        for i in range(0, col):
            for j in range(0, row):
                #makes the id of the node a string value
                nodeid = str(i) + str(j)
                #appends each node to the list setting the dims to equal i and j
                #and nodeid to equal the string value of the position starting at 00
                self.nodelist.append(Node([i, j], nodeid))

    def getnode(self, nodeid):
        '''gets a node in the graph at value of [1,1]'''
        #returns the id of the node in the list
        return self.nodelist[nodeid]

def getneighbors(node, graph):
    '''gets the node value of neighbors to your current node'''
    #neighbor directions from the current node, pretty self explanitory
    right = [1, 0]
    left = [-1, 0]
    top = [0, 1]
    bottom = [0, -1]
    topright = [1, 1]
    bottomright = [1, -1]
    topleft = [-1, 1]
    bottomleft = [-1, -1]
    #generates a list for all the neighbors to the given node
    neighbors = []
    #a list to give the program data on which nodes to look for
    childnodes = [right, left, top, bottom,
                  topleft, topright, bottomleft, bottomright]
    #loop adding the directional position of the neighbor nodes to the current node
    for i in childnodes:
        item1 = i[0] + node.value[0]
        item2 = i[1] + node.value[1]
        #gets the id of the neighbors using the getnode function
        grab_node = graph.getNode([item1, item2])
        #conditional evaluating if there are neighbors and if those neighbors are walkable
        if grab_node is not None and grab_node.walkable:
            #if evaluated to true, append the neighbor's id to the neighbors list
            neighbors.append(grab_node)
    #returns the list
    return neighbors

def astar(start, goal, graph):
    '''this is our pathfinder, hopefully'''
    #makes a list for the open queue
    openlist = []
    #makes a list for the closed queue
    closelist = []
    #makes a list for the path chosen
    path = []
    #not sure yet
    came_from = None
    #sets the current node to equal the starting node
    current = start
    #adds the current node to the open queue
    openlist.append(current)
    #loop stating that while there are objects in the open queue, to do stuff
    while openlist is not None:
        #removes the current node from the open queue because it is found
        openlist.remove(current)
        #puts the current node in the closed list
        closelist.append(current)
        #calls the getneighbor function using the current node
        #to initialize all the neighbors adjacent to the current node in the neighbors list
        current.neighbors = getneighbors(current, graph)
        for node in current.neighbors:
            if node not in closelist:
                openlist.append(node)
                gvalue(current, node)
                hvalue(node, goal)
                fvalue(node)
        openlist.sort(key=lambda node: node.fscore)
        came_from = current
        path.append(came_from)
        current = openlist[0]
        return path

#things to do for astar
#need to retrace
#need to add parent
