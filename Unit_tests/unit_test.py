#Unit Test of the system
#from a_estrella import *
from tec.ic.ia.pc2.g09 import * 



"""
#The bunny can move from a position to other position
def test_bunny_moves():
	field_list_test = store_field_list("entrada.txt")
	bunny_test = Bunny(5)
	bunny_test.find_bunny(field_list_test)
	field_test = Field()
	field_test.field_list = field_list_test
	assert bunny_test.move("RIGTH", field_test.field_list) == field_list_test


#The bunny eats the carrot
def test_bunny_eat():


# The bunny choose the path with a low f(n)
#def test_bunny_choose_path():


# The system can show the travel of the bunny
#def show_bunny_travel():
"""

"""
Unit tests for the genetic algorithm
"""

# if the direction is right the rabbit must eat one carrot and walk 5 steps
def test_one_row_file_right():
	with open("one_row.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
		entrada = list(csv.reader(csvarchivo))
		startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,12,100,"best",0.3)
		carrots, steps = searchCarrots(entrada[:len(entrada)-1], Dir.RIGHT, 1, 0)
		print(carrots,steps)
		assert carrots == 1 and steps == 5

# if the direction is left the rabbit must eat zero carrots and walk 2 steps
def test_one_row_file_left():
	with open("one_row.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
		entrada = list(csv.reader(csvarchivo))
		startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,12,100,"best",0.3)
		carrots, steps = searchCarrots(entrada[:len(entrada)-1], Dir.LEFT, 1, 0)
		print(carrots,steps)
		assert carrots == 0 and steps == 2

# if the direction is ip the rabbit must eat zero carrots and walk 0 steps
def test_one_row_file_up():
	with open("one_row.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
		entrada = list(csv.reader(csvarchivo))
		startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,12,100,"best",0.3)
		carrots, steps = searchCarrots(entrada[:len(entrada)-1], Dir.UP, 1, 0)
		print(carrots,steps)
		assert carrots == 0 and steps == 1

# if the individual doesn't have mutations it must return the individual mutated
def test_mutation():
	with open("mutation.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
		entrada = list(csv.reader(csvarchivo))
		startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,12,100,"best",0.3)		
		tmp = []
		tmp2 = []
		for j in range(len(entrada[:len(entrada)-1])):
		    tmp2.append(entrada[:len(entrada)-1][j].copy())
		tmp.append(tmp2)
		tmp.append([[],[]])
		tmp.append(0)
		tmp.append([2,7])
		tmp.append(0)
		tmp = mutate(tmp,1)
		assert tmp[2] == 1


# if the individual has a mutation it must return the individual with a modification or without mutations
def test_mutation():
	with open("mutation.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
		entrada = list(csv.reader(csvarchivo))
		startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,12,100,"best",0.3)		
		tmp = []
		tmp3 = []
		tmp2 = []
		tmp4 = []
		for j in range(len(entrada[:len(entrada)-1])):
			tmp2.append(entrada[:len(entrada)-1][j].copy())
		tmp.append(tmp2)
		tmp.append([[],[]])
		tmp.append(0)
		tmp.append([2,7])
		tmp.append(0)
		tmp = mutate(tmp,1)
		for j in range(len(tmp[0])):
			tmp4.append(tmp[0][j].copy())
		tmp3.append(tmp4)
		tmp3.append([tmp[1][0].copy(),tmp[1][1].copy()])
		tmp3.append(tmp[2])
		tmp3.append([tmp[3][0],tmp[3][1]])
		tmp3.append(tmp[4])
		tmp = mutate(tmp,1)
		assert  tmp[0] != tmp3[0] 

# if 2 individual crosses the children must have the same size
def test_cross():
	with open("cross.txt") as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
		entrada = list(csv.reader(csvarchivo))
		startGenetic(entrada[:len(entrada)-1],Dir.RIGHT,12,100,"best",0.3)		
		tmp = []
		tmp3 = []
		tmp2 = []
		tmp4 = []
		for j in range(len(entrada[:len(entrada)-1])):
			tmp2.append(entrada[:len(entrada)-1][j].copy())
		tmp.append(tmp2)
		tmp.append([[],[]])
		tmp.append(0)
		tmp.append([2,7])
		tmp.append(0)
		tmp = mutate(tmp,1)
		for j in range(len(tmp[0])):
			tmp4.append(tmp[0][j].copy())
		tmp3.append(tmp4)
		tmp3.append([tmp[1][0].copy(),tmp[1][1].copy()])
		tmp3.append(tmp[2])
		tmp3.append([tmp[3][0],tmp[3][1]])
		tmp3.append(tmp[4])
		tmp = mutate(tmp,1)
		tmp = mutate(tmp,1)
		tmp = mutate(tmp,1)
		tmp = mutate(tmp,1)
		tmp3 = mutate(tmp3,1)
		tmp3 = mutate(tmp3,1)
		tmp3 = mutate(tmp3,1)
		tmp3 = mutate(tmp3,1)
		a, b = cross(tmp[0],tmp3[0])
		assert  len(a[0]) == len(tmp[0]) and len(a[0][0]) == len(tmp[0][0]) and len(b[0]) == len(tmp[0]) and len(b[0][0]) == len(tmp[0][0])

