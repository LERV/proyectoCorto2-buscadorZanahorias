import csv # Para abrir el archivo csv y cargar los datos
from enum import Enum
import random  # Para generar numeros aleatorios
import os
import sys
import shutil 

class Dir(Enum):
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4


x, y, rx, ry, carrotsGoal = 0, 0, 0, 0, 0
bestBoard = None
enter = ""
def generate_csv(lista, generation, individual, direction):
    dire = ""
    if(direction == Dir.RIGHT):
        dire = "derecha"
    elif(direction == Dir.LEFT):
        dire = "izquierda"
    elif(direction == Dir.UP):
        dire = "arriba"
    elif(direction == Dir.DOWN):
        dire = "abajo"
    while(len(generation) != 5):
        generation = "0" + generation
    while(len(individual) != 5):
        individual = "0" + individual
    try:  
        path = os.getcwd()
        os.makedirs(path + "/" + dire + "/" + generation)
    except OSError:
        8+2
    myFile = open(dire + "/" + generation + "/" + individual + '.txt', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(lista)

def generatePopulation(board, population_length, elements):
    population = []
    for i in range(population_length):
        tmp = []
        tmp2 = []
        for j in range(len(board)):
            tmp2.append(board[j][:])
        tmp.append(tmp2)
        tmp.append([[],[]])
        tmp.append(0)
        tmp.append(elements[:])
        tmp.append(0)
        population.append(tmp[:])
    return population

def findElements(board):
    leftCounter = 0
    rightCounter = 0
    global enter
    global x
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == "C"):
                global rx
                global ry
                rx, ry = j, i
                if(j < x // 2):
                    leftCounter += 1
                else:
                    rightCounter += 1
            elif(board[i][j] == "Z"):
                global carrotsGoal
                carrotsGoal += 1
                if(j < x // 2):
                    leftCounter += 1
                else:
                    rightCounter += 1
            elif(board[i][j] == enter):
                if(j < x // 2):
                    leftCounter += 1
                else:
                    rightCounter += 1
    return [leftCounter, rightCounter]

#def cross():

def mutate(board,mutationRate):
    rand = random.random()
    global x
    global y
    if(rand <= mutationRate):
        #print("Mutacion")
        if((rand <= mutationRate / 3 and board[3][0] + board[3][1] != x * y) or board[2] == 0):
            while(True):
                tmpX = int(random.random() * x)
                tmpY = int(random.random() * y)
                if(board[0][tmpY][tmpX] == " "):
                    val = int(random.random() * 4)
                    if(val == 0):
                        board[0][tmpY][tmpX] = "A"
                    elif(val == 1):
                        board[0][tmpY][tmpX] = "V"
                    elif(val == 2):
                        board[0][tmpY][tmpX] = "<"
                    else:
                        board[0][tmpY][tmpX] = ">"
                    if(tmpX < x // 2):
                        board[1][0].append([tmpX,tmpY])
                        board[3][0] += 1
                    else:
                        board[1][1].append([tmpX,tmpY])
                        board[3][1] += 1
                    board[2] += 1
                    break
        elif(rand > mutationRate / 3 and rand <= mutationRate * 2 / 3):
            index = int(random.random() * board[2])
            if(index < len(board[1][0])):   
                while(True):
                    val = int(random.random() * 4)
                    if(val == 0 and board[0][board[1][0][index][1]][board[1][0][index][0]] != "A"):
                        board[0][board[1][0][index][1]][board[1][0][index][0]] = "A"
                        break
                    elif(val == 1 and board[0][board[1][0][index][1]][board[1][0][index][0]] != "V"):
                        board[0][board[1][0][index][1]][board[1][0][index][0]] = "V"
                        break
                    elif(val == 2 and board[0][board[1][0][index][1]][board[1][0][index][0]] != "<"):
                        board[0][board[1][0][index][1]][board[1][0][index][0]] = "<"
                        break
                    elif(val == 3 and board[0][board[1][0][index][1]][board[1][0][index][0]] != ">"):
                        board[0][board[1][0][index][1]][board[1][0][index][0]] = ">"
                        break
            else:
                while(True):
                    val = int(random.random() * 4)
                    if(val == 0 and board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] != "A"):
                        board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] = "A"
                        break
                    elif(val == 1 and board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] != "V"):
                        board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] = "V"
                        break
                    elif(val == 2 and board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] != "<"):
                        board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] = "<"
                        break
                    elif(val == 3 and board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] != ">"):
                        board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] = ">"
                        break
        else:
            index = int(random.random() * board[2])
            if(index < len(board[1][0])):   
                board[0][board[1][0][index][1]][board[1][0][index][0]] = " "
                board[1][0].pop(board[1][0].index(board[1][0][index]))
                board[3][0] -= 1
            else:
                board[0][board[1][1][index-len(board[1][0])][1]][board[1][1][index-len(board[1][0])][0]] = " "
                board[1][1].pop(board[1][1].index(board[1][1][index-len(board[1][0])]))
                board[3][1] -= 1
            board[2] -= 1
    return board


def cross(board1, board2):
    a = []
    b = []
    for i in range(len(board1)):
        tmpA = []
        tmpB = []
        for j in range(len(board1[0])):
            if(j < x // 2):
                tmpA.append(board1[i][j])
                tmpB.append(board2[i][j])
            else:
                tmpA.append(board2[i][j])
                tmpB.append(board1[i][j])
        a.append(tmpA)
        b.append(tmpB)
    return [a], [b]

def crossing(population,crossingPolicy):
    newPopulation = []
    if(crossingPolicy == "best"):
        offset = 0
        for i in range(len(population) // 2):
            a, b = cross(population[i + offset][0], population[i + offset + 1][0])
            a.append([population[i + offset][1][0], population[i + offset + 1][1][1]])
            b.append([population[i + offset + 1][1][0], population[i + offset][1][1]])
            a.append(len(population[i + offset][1][0]) + len(population[i + offset + 1][1][1]))
            b.append(len(population[i + offset + 1][1][0]) + len(population[i + offset][1][1]))
            a.append([population[i + offset][3][0], population[i + offset + 1][3][1]])
            b.append([population[i + offset + 1][3][0], population[i + offset][3][1]])
            a.append(0)
            b.append(0)
            newPopulation.append(a)
            newPopulation.append(b)
            offset += 1
        #for u in range(len(newPopulation)):
            #print(newPopulation[u])
    else:
        #print(" ")
        length = len(population) - 1
        for i in range(len(population) // 2):
            a, b = cross(population[i][0], population[length - i][0])
            a.append([population[i][1][0], population[length - i][1][1]])
            b.append([population[length - i][1][0], population[i][1][1]])
            a.append(len(population[i][1][0]) + len(population[length - i][1][1]))
            b.append(len(population[length - i][1][0]) + len(population[i][1][1]))
            a.append([population[i][3][0], population[length - i][3][1]])
            b.append([population[length - i][3][0], population[i][3][1]])
            a.append(0)
            b.append(0)
            newPopulation.append(a)
            newPopulation.append(b)
        #for u in range(len(newPopulation)):
            #print(newPopulation[u])
    return newPopulation

def startGenetic(board, direction, population_length, generations):
    global x
    global y
    global rx
    global ry
    global carrotsGoal
    global bestBoard
    dire = ""
    if(direction == Dir.RIGHT):
        dire = "derecha"
    elif(direction == Dir.LEFT):
        dire = "izquierda"
    elif(direction == Dir.UP):
        dire = "arriba"
    elif(direction == Dir.DOWN):
        dire = "abajo"
    try:
        shutil.rmtree(dire)
    except OSError:
        print ("Error")
    y = len(board)
    x = len(board[0])
    enter = board[0][x-1]
    print("Cuadricula (x,y) ",x,y)
    elements = findElements(board)
    population = generatePopulation(board, population_length, elements)
    #print(population)
    for generation in range(generations):
        #print(generation)
        population = sorted(population, key=lambda item: item[4])
        #for u in range(len(population)):
            #print(u,population[u])
        population = crossing(population,"best")
        for i in range(len(population)):
            tmp = []
            tmp2 = []
            for j in range(len(population[i][0])):
                tmp2.append(population[i][0][j][:])
            tmp.append(tmp2)
            tmp2 = []
            tmp2.append(population[i][1][0][:])
            tmp2.append(population[i][1][1][:])
            tmp.append(tmp2)
            tmp.append(population[i][2])
            tmp.append(population[i][3][:])
            tmp.append(population[i][4])
            mutatedIndividual = mutate(tmp,0.3)
            #print("tmp",mutatedIndividual)
            #print("population i 0",population[i])
            #print(searchCarrots(population[i][0], direction, rx, ry))
            carrots, steps = searchCarrots(population[i][0], direction, rx, ry)
            population[i][4] = population[i][2] + 10 * (carrotsGoal - carrots) + steps / 4 
            carrotsMutated, stepsMutated = searchCarrots(mutatedIndividual[0], direction, rx, ry)
            mutatedIndividual[4] = mutatedIndividual[2] + 10 * (carrotsGoal - carrotsMutated) + stepsMutated / 4
            #print(mutatedIndividual)
            #population[i] = mutatedIndividual
            
            if(mutatedIndividual[4] < population[i][4]):
                population[i] = mutatedIndividual
            
            if(bestBoard == None or bestBoard[4] > population[i][4]):
                bestBoard = population[i]
                bestBoard.append(generation)
                bestBoard.append(i)
            generate_csv(population[i][0], str(generation), str(i), direction)
    print("Mejor")
    print(bestBoard)


def move(r_x, r_y, direction):
    if(direction == Dir.UP):
        r_y -= 1
    elif(direction == Dir.DOWN):
        r_y += 1
    elif(direction == Dir.RIGHT):
        r_x += 1
    else:
        r_x -= 1
    return r_x, r_y


def searchCarrots(board, direction, r_x, r_y, carrots = 0, steps = 1, changed = False):
    r_x, r_y = move(r_x, r_y, direction)
    global x
    global y
    global enter
    #print("rabbit (x,y)", r_x, r_y, steps, carrots, changed, direction)
    #print(board)
    if(r_x < x and r_y < y and board[r_y][r_x] != enter and r_x >= 0 and r_y >= 0):
        if(board[r_y][r_x] != " "):
            if(board[r_y][r_x] == "Z"):
                return searchCarrots(board, direction, r_x, r_y, carrots+1, steps+1, changed)
            elif(board[r_y][r_x] == "A"):
                if(changed and direction == Dir.DOWN):
                    return carrots, 1000000000
                else:
                    return searchCarrots(board, Dir.UP, r_x, r_y, carrots, steps+1, True)
            elif(board[r_y][r_x] == "V"):
                if(changed and direction == Dir.UP):
                    return carrots, 1000000000
                else:
                    return searchCarrots(board, Dir.DOWN, r_x, r_y, carrots, steps+1, True)
            elif(board[r_y][r_x] == ">"):
                if(changed and direction == Dir.LEFT):
                    return carrots, 1000000000
                else:
                    return searchCarrots(board, Dir.RIGHT, r_x, r_y, carrots, steps+1, True)
            elif(board[r_y][r_x] == "<"):
                if(changed and direction == Dir.RIGHT):
                    return carrots, 1000000000
                else:
                    return searchCarrots(board, Dir.LEFT, r_x, r_y, carrots, steps+1, True)
            else:
                return searchCarrots(board, direction, r_x, r_y, carrots, steps+1, changed)
        else:
            return searchCarrots(board, direction, r_x, r_y, carrots, steps+1, changed)
    else:
        return carrots, steps



sys.setrecursionlimit(1000000000)

with open("entrada.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
    entrada = list(csv.reader(csvarchivo))
    startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,1000,10000)
