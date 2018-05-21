# Program for search carrots in a land by a bunny


#Class that defines the land of carrots with a bunny
class Land:
	land_lengh = None 
	land_width = None
	carrots_count = None
	bunny = None
	land_list = []

	#def __init__(self, ):


#class Bunny:

def create_land():
	land = Land()

		
#Fuction that reads and print a file, the non-traveled land
def read_file(filename):
	file_object = open(filename, "r")
	#print (file_object.read())
	return file_object


#Function that store a open file in
def store_land_list(filename):
	land_list = []
	land_file = read_file(filename)
	for line in land_file:
		land_list.append((line.split(','))[:-1])
	print(land_list)
	return write_file(5, land_list)

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

store_land_list("entrada.txt")





