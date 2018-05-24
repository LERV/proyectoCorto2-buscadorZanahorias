from heapq import heappush, heappop # for priority queue
import math
import time
import random

##    cost is sometimes written as w or d or l or length
##    cost_so_far is usually written as g or d or distance
##    heuristic is usually written as h
##    In A*, the priority is usually written as f, where f = g + h
##    came_from is sometimes written as π or parent or previous or prev
##    frontier is usually called OPEN
##    visited is the union of OPEN and CLOSED
##    locations such as current and next are written with letters u, v

#Class that defines the field of carrots with a bunny
class Field:
    field_length = None 
    field_width = None
    carrots_count = None
    bunny_position = (0,0)
    field_list = [] #List map
    carrots_position_list = []


    #Function that construct the class field
    def __init__(self,filename):
        self.field_length = 0
        self.field_width = 0
        self.carrots_count = 0
        self.store_field_list(filename) 
        self.locate_carrots()
        self.find_bunny()

    #Funcion that locate the carrots in the field
    def locate_carrots(self):
        for i in range(len(self.field_list)):
            for j in range(len(self.field_list[i])):
                if self.field_list[i][j] == "Z":
                    self.carrots_position_list.append((i,j))
        print("Position of carrots found: ", self.carrots_position_list)

    def find_bunny(self):
        for i in range(len(self.field_list)):
            for j in range(len(self.field_list[i])):
                #print("Va,i,j",self.field_list[i][j],i,j)
                if self.field_list[i][j] == "C":
                    self.bunny_position=(i,j)

        print("Bunny position: ", self.bunny_position)

    #Function that store a open file in
    def store_field_list(self,filename):      
        field_file = open(filename, "r")
        for line in field_file:
            self.field_list.append((line.split(','))[:-1])
        print(self.field_list)

class node:
    xPos = 0 # x position
    yPos = 0 # y position
    distance = 0 # Cost: g(n) total distance already travelled to reach the node
    priority = 0 # f(n) priority = distance + remaining distance estimate
    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
    def __lt__(self, other): # comparison method for priority queue
        return self.priority < other.priority
    
    def updatePriority(self, xDest, yDest):
        #f(n)=g(n)+h(n)
        self.priority = self.distance + self.estimate(xDest, yDest) * 10 # A*
    # give higher priority to going straight instead of diagonally
    def nextMove(self, dirs, d): # d: direction to move
        self.distance += 10
    # Estimation function for the remaining distance to the goal.
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        # Euclidian Distance
        d = math.sqrt(xd * xd + yd * yd)
        # Manhattan distance
        # d = abs(xd) + abs(yd)
        # Chebyshev distance
        # d = max(abs(xd), abs(yd))
        return(d)

# A-star algorithm.
# The path returned will be a string of digits of directions.
def pathFind(the_map, n, m, dirs, dx, dy, xA, yA, xB, yB):
    closed_nodes_map = [] # map of closed (tried-out) nodes
    open_nodes_map = [] # map of open (not-yet-tried) nodes
    dir_map = [] # map of dirs
    row = [0] * n
    for i in range(m): # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []] # priority queues of open (not-yet-tried) nodes
    pqi = 0 # priority queue index
    # create the start node and push into list of open nodes
    n0 = node(xA, yA, 0, 0)
    n0.updatePriority(xB, yB)
    heappush(pq[pqi], n0)
    open_nodes_map[yA][xA] = n0.priority # mark it on the open nodes map

    # A* search
    while len(pq[pqi]) > 0:
        # get the current node w/ the highest priority
        # from the list of open nodes
        n1 = pq[pqi][0] # top node
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi]) # remove the node from the open list
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1 # mark it on the closed nodes map

        # quit searching when the goal is reached
        # if n0.estimate(xB, yB) == 0:
        if x == xB and y == yB:
            # generate the path from finish to start
            # by following the dirs
            path = ''
            while not (x == xA and y == yA):
                j = dir_map[y][x]
                c = str((j + dirs // 2) % dirs)
                print("Si llega...-C:",c," -j:",j," -dirs",dirs)
                print("x,y:",x,y)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path

        # generate moves (child nodes) in all possible dirs
        for i in range(dirs):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m - 1
                    or the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                # generate a child node
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(dirs, i)
                m0.updatePriority(xB, yB)
                # if it is not in the open list then add into that
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    # mark its parent node direction
                    dir_map[ydy][xdx] = (i + dirs // 2) % dirs
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction
                    dir_map[ydy][xdx] = (i + dirs // 2) % dirs
                    # replace the node
                    # by emptying one pq to the other one
                    # except the node to be replaced will be ignored
                    # and the new node will be pushed in instead
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi]) # remove the target node
                    # empty the larger size priority queue to the smaller one
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1-pqi], pq[pqi][0])
                        heappop(pq[pqi])       
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) # add the better node instead
    return 'No route found' # if no route found

# MAIN
#****************************Generacion de mapa*******************************
nuevoCampo=Field("entrada.txt")
print("***************************************************************")

print("Mapa:",nuevoCampo.field_list)
print("Pos zanahorias",nuevoCampo.carrots_position_list)
print("Conejo pos:",nuevoCampo.bunny_position)

input('Press Enter...')
#******************************************************************************

dirs = 4 # number of possible directions to move on the map


dx = [1, 0, -1, 0] #Derecha=1 Izquierda=-1
dy = [0, 1, 0, -1] #Abajo


n = 30 # horizontal size of the map
m = 30 # vertical size of the map
the_map = []
row = [0] * n  #Mapa esta lleno de 0 por defecto
for i in range(m): # create empty map
    the_map.append(list(row))


(xA, yA, xB, yB) = (3,4,20,20) #Points Start and Finish
#(xA, yA, xB, yB) = (nuevoCampo.bunny_position[0],nuevoCampo.bunny_position[1],nuevoCampo.carrots_position_list[0][0],nuevoCampo.carrots_position_list[][]) #Points Start and Finish

print ('Map size (X,Y): ', n, m)
print ('Start: ', xA, yA)
print ('Finish: ', xB, yB)
t = time.time()

#the_map es un matriz que tiene nuestra info
route = pathFind(the_map, n, m, dirs, dx, dy, xA, yA, xB, yB)
print ('Time to generate the route (seconds): ', time.time() - t)
print ('Route:')
print ("rura:",route)

# mark the route on the map
if len(route) > 0:
    x = xA
    y = yA
    the_map[y][x] = 2
    for i in range(len(route)):
        j = int(route[i])
        x += dx[j]
        y += dy[j]
        the_map[y][x] = 3
    the_map[y][x] = 4

# display the map with the route added
print ('Map:')
for y in range(m):
    for x in range(n):
        xy = the_map[y][x]
        if xy == 0:
            print ('.',end="") # space
        elif xy == 1:
            print ('O',end="") # obstacle
        elif xy == 2:
            print ('S',end="") # start
        elif xy == 3:
            print ('R',end="") # route
        elif xy == 4:
            print ('F',end="") # finish
    print()

#Busco todoas Z, y me voy a la primera
#Ver ? rango vision
#Desde donde encontró Z vuelve a buscar otra zanahoriái
#En next move generar txt

#****************************Generacion de mapa*******************************
nuevoCampo=Field("entrada.txt")
print("***************************************************************")

print("Mapa:",nuevoCampo.field_list)
print("Pos zanahorias",nuevoCampo.carrots_position_list)
print("Conejo pos:",nuevoCampo.bunny_position)

input('Press Enter...')
#******************************************************************************
