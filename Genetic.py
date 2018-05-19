import csv # Para abrir el archivo csv y cargar los datos
from enum import Enum
import random  # Para generar numeros aleatorios

class Dir(Enum):
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4


x, y, rx, ry, carrotsGoal = 0, 0, 0, 0, 0
bestBoard = None
enter = ""
def generar_csv(lista):
    myFile = open('prueba.txt', 'w')
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
    return [[a]], [[b]]

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
        for u in range(len(newPopulation)):
            print(newPopulation[u])
    else:
        print(" ")
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
        for u in range(len(newPopulation)):
            print(newPopulation[u])
    return newPopulation

def startGenetic(board, direction, population_length, generations):
    global x
    global y
    global rx
    global ry
    y = len(board)
    x = len(board[0])
    enter = board[0][x-1]
    print("Cuadricula (x,y) ",x,y)
    elements = findElements(board)
    population = generatePopulation(board, population_length, elements)
    

    for u in range(10):
        for w in range(10):
            print(u,w,population[w])
            tmp = []
            tmp2 = []
            for j in range(len(population[w][0])):
                tmp2.append(population[w][0][j][:])
            tmp.append(tmp2)
            tmp2 = []
            tmp2.append(population[w][1][0][:])
            tmp2.append(population[w][1][1][:])
            tmp.append(tmp)
            tmp.append(population[w][2])
            tmp.append(population[w][3][:])
            tmp.append(population[w][4])
            mutate(tmp,0.3)
            print(u,w,population[w])
        
    for u in range(len(population)):
        print(population[u])
    crossing(population,"inverted")
    """
    for generation in range(generations):
        population = sorted(population, key=lambda item: item[4])

     
            carrots, steps = searchCarrots(population[i][0], direction, rx, ry)
    """    


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


def searchCarrots(board, direction, r_x, r_y, carrots = 0, steps = 1):
    r_x, r_y = move(r_x, r_y, direction)
    global x
    global y
    global enter
    print("rabbit (x,y)", r_x, r_y, steps, carrots)
    if(r_x < x and r_y < y and board[r_y][r_x] != enter and r_x >= 0 and r_y >= 0):
        if(board[r_y][r_x] != " "):
            if(board[r_y][r_x] == "Z"):
                searchCarrots(board, direction, r_x, r_y, carrots+1, steps+1)
            elif(board[r_y][r_x] == "A"):
                searchCarrots(board, Dir.UP, r_x, r_y, carrots, steps+1)
            elif(board[r_y][r_x] == "V"):
                searchCarrots(board, Dir.DOWN, r_x, r_y, carrots, steps+1)
            elif(board[r_y][r_x] == ">"):
                searchCarrots(board, Dir.RIGHT, r_x, r_y, carrots, steps+1)
            elif(board[r_y][r_x] == "<"):
                searchCarrots(board, Dir.LEFT, r_x, r_y, carrots, steps+1)
        else:
            searchCarrots(board, direction, r_x, r_y, carrots, steps+1)
    else:
        return carrots, steps





with open("entrada.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
    entrada = list(csv.reader(csvarchivo))
    print(entrada[:len(entrada)-1])
    generar_csv(entrada)
    startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,10,5)
