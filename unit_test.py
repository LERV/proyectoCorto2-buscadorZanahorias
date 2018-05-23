#Unit Test of the system
from a_estrella import *

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

