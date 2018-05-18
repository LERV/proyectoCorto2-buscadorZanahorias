import csv # Para abrir el archivo csv y cargar los datos
from enum import Enum
import random  # Para generar numeros aleatorios

class Dir(Enum):
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4

        
x, y, rx, ry = 0, 0, 0, 0
enter = ""
def generar_csv(lista):
    myFile = open('prueba.txt', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(lista)

def generatePopulation(board, population_length):
    population = []
    for i in range(population_length):
        population.append(board)
    return population

def findRabbit(board):
    rx, ry = 0, 0
    flag = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == "C"):
                global rx
                global ry
                rx, ry, flag = i, j, True
                break
        if(flag):
            break

def startGenetic(board, direction, population_length, generations):
    global x
    global y
    y = len(board) 
    x = len(board[0])
    enter = board[0][x-1]
    print("Cuadricula (x,y) ",x,y)
    generatePopulation(board, population_length)
    findRabbit(board)
    searchCarrots(board, direction, rx, ry)
    
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


"""
Entrada: max es un numero que resepresenta el valor maximo a generar.
Salida: Un numero aleatorio generado.
Restriccion: El numero n debe ser mayor a 0, pero en el codigo programado no aplica.
Genera una mnumero aleatorio mayor a 0 y menor que max.
"""

def generate_random(max):
    return int(random.random() * max)
