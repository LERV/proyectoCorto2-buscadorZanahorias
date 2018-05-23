# Program for search carrots in a land by a bunny

import random

#Class that defines the land of carrots with a bunny
class Land:
	land_length = None 
	land_width = None
	carrots_count = None
	bunny = None
	land_list = []
	land_carrots_position = []


	#Function that construct the class Land
	def __init__(self):
		self.land_length = 0
		self.land_width = 0
		self.carrots_count = 0 

	#Funcion that locate the carrots in the land
	def locate_carrots(self, land_list):
		carrots_position_list = []
		for i in range(len(land_list)):
			for j in range(len(land_list[i])):
				if land_list[i][j] == "Z":
					carrots_position_list.append([i,j])
		print("Position of carrots found: ", carrots_position_list)
		return carrots_position_list
	
#Function that define the A* Algorithm
class A_star:
	land_heuristic_list = []

	def __init__(self):
		self.land_heuristic_list = []

	def calculate_heuristic_land(self, land_list, bunny_vision):
		#Fill the land with "N's", after it will be fill of h's cost
		for i in range(3):
			position_list = []
			for j in range(3):
				position_list.append(random_heuristic())
			land_heuristic_list.append(position_list)
		print (self.land_heuristic_list)
		return self.land_heuristic_list		

#Class that define the attributes of the bunny
class Bunny:
	vision_distance = 0
	bunny_sign = "C"

	def __init__(self, vision_distance):
		self.vision_distance = vision_distance

	#Function that move 
	"""def move(self, direction, land_list):
		moved_state = None
		for i in range(len(land)):

		return land_list"""

	#Function that find the bunny in the land
	def find_bunny(self, land_list):
		bunny_position = []
		for i in range(len(land_list)):
			for j in range(len(land_list[0])):
				if land_list[i][j] == "C":
					bunny_position.append(i)
					bunny_position.append(j)
		print("Bunny position: ", bunny_position)
		return bunny_position


def random_heuristic():
	random_var = random.randint(0,10)
	return random_var
		
#Fuction that reads and print a file, the non-traveled land
def read_file(filename):
	file_object = open(filename, "r")
	#print (file_object.read())
	return file_object

#Function that calculate the length of the land (X Axis)
def calculate_land_length(land_list):
	land_lengt = len(land_list[0])
	return land_lengt

#Function that calculate the width of the land (Y Axis)
def calculate_land_width(land_list):
	land_width = len(land_list)
	return land_width

#Function that store a open file in
def store_land_list(filename):
	land_list = []
	land_file = read_file(filename)
	for line in land_file:
		land_list.append((line.split(','))[:-1])
	print(land_list)
	return land_list

#Function that writes a list in a file
def write_file(number, list):
	file_object = open("file"+str(number)+".txt", 'w')
	for i in range(len(list)):
		string_line = ""
		for j in range(len(list[0])):
			string_line = string_line + list[i][j] + ","
		string_line = string_line + "\n"
		file_object.write(string_line)
	file_object.close()



#START HERE!!!


land_list = store_land_list("entrada.txt")
bunny_test = Bunny(5) #Bunny with a vision distance of 5 units
bunny_test.find_bunny(land_list)
land_test = Land()
land_test.locate_carrots(land_list)
#a_star_test = A_star()
#a_star_test.calculate_heuristic_land(5, land_list)








