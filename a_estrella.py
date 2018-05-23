# Program for search carrots in a field by a bunny

import random

#Class that defines the field of carrots with a bunny
class Field:
	field_length = None 
	field_width = None
	carrots_count = None
	bunny = None
	field_list = []
	field_carrots_position = []


	#Function that construct the class field
	def __init__(self):
		self.field_length = 0
		self.field_width = 0
		self.carrots_count = 0 

	#Funcion that locate the carrots in the field
	def locate_carrots(self):
		carrots_position_list = []
		for i in range(len(self.field_list)):
			for j in range(len(self.field_list[i])):
				if self.field_list[i][j] == "Z":
					carrots_position_list.append([i,j])
		print("Position of carrots found: ", carrots_position_list)
		return carrots_position_list
	
#Function that define the A* Algorithm
class A_star:
	field_heuristic_list = []

	def __init__(self):
		self.field_heuristic_list = []

	def calculate_heuristic_field(self, field_list, bunny_vision):
		#Fill the field with "N's", after it will be fill of h's cost
		for i in range(3):
			position_list = []
			for j in range(3):
				position_list.append(random_heuristic())
			field_heuristic_list.append(position_list)
		print (self.field_heuristic_list)
		return self.field_heuristic_list		

#Class that define the attributes of the bunny
class Bunny:
	vision_distance = 0
	bunny_sign = "C"
	bunny_position = []

	def __init__(self, vision_distance):
		self.vision_distance = vision_distance

	#Function that move the bunny across the carrot's field
	def move(self, direction, field_list):
		moved_state = None
		if direction == "LEFT" and self.bunny_position[1] > 0:
			field_list[self.bunny_position[0]][self.bunny_position[1]-1] = "C"
			field_list[self.bunny_position[0]][self.bunny_position[1]] = ""
			self.bunny_position = self.find_bunny(field_list)
			print(field_list)
			return field_list

		if direction == "RIGTH" and self.bunny_position[1] < len(field_list[1])-2:
			field_list[self.bunny_position[0]][self.bunny_position[1]+1] = "C"
			field_list[self.bunny_position[0]][self.bunny_position[1]] = ""
			self.bunny_position = self.find_bunny(field_list)
			print(field_list)
			return field_list

		if direction == "UP" and self.bunny_position[0] > 0:
			field_list[self.bunny_position[0]-1][self.bunny_position[1]] = "C"
			field_list[self.bunny_position[0]][self.bunny_position[1]] = ""
			self.bunny_position = self.find_bunny(field_list)
			print(field_list)
			return field_list			
		
		if direction == "DOWN" and self.bunny_position[0]< len(field_list[0]-2):
			field_list[self.bunny_position[0]-1][self.bunny_position[1]] = "C"
			field_list[self.bunny_position[0]][self.bunny_position[1]] = ""
			self.bunny_position = self.find_bunny(field_list)
			print(field_list)
			return field_list

	#Function that find the bunny in the field
	def find_bunny(self, field_list):
		bunny_position = []
		for i in range(len(field_list)):
			for j in range(len(field_list[0])):
				if field_list[i][j] == "C":
					bunny_position.append(i)
					bunny_position.append(j)
		print("Bunny position: ", bunny_position)
		self.bunny_position = bunny_position
		return bunny_position

#Function that calculate the heuristic of a node
def random_heuristic():
	random_var = random.randint(0,10)
	return random_var
		
#Fuction that reads and print a file, the non-traveled field
def read_file(filename):
	file_object = open(filename, "r")
	#print (file_object.read())
	return file_object

#Function that calculate the length of the field (X Axis)
def calculate_field_length(field_list):
	field_lengt = len(field_list[0])
	return field_lengt

#Function that calculate the width of the field (Y Axis)
def calculate_field_width(field_list):
	field_width = len(field_list)
	return field_width

#Function that store a open file in
def store_field_list(filename):
	field_list = []
	field_file = read_file(filename)
	for line in field_file:
		field_list.append((line.split(','))[:-1])
	print(field_list)
	return field_list

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
field_list_test = store_field_list("entrada.txt")
bunny_test = Bunny(5) #Bunny with a vision distance of 5 units
bunny_test.find_bunny(field_list_test)
field_test = Field()
field_test.field_list = field_list_test
field_test.locate_carrots()
bunny_test.move("RIGTH", field_test.field_list)
#a_star_test = A_star()
#a_star_test.calculate_heuristic_field(5, field_list)