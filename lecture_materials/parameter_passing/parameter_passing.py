'''
Class: CSC 131
Author: Sam Bumgardner
Purpose: Give different parameter passing examples.

To use, first navigate your command line to where this file is located, then run the following command:
	python parameter_passing.py
'''

'''
Basic parameter usage examples:
'''

# If a function doesn't take parameters, it typically does the exact same thing every time.
def one_plus_two():
	sum = 1 + 2
	return sum

# If a function does take parameters, its results can be more flexible.
def simple_add(num_1, num_2):
	sum = num_1 + num_2
	return sum

# You can think of a function like a recipe, and the parameters, ingredients.
def name_three_part_sandwich(food_1, food_2, food_3):
	return food_1 + " " + food_2 + " and " + food_3 + " sandwich"

# Sometimes functions are useful a grouping tool, even if you don't let it have any parameters.
def basic_parameters_example():
	print()
	print("An example of calling one_plus_two() with no parameters:")
	print(str(one_plus_two()), end="\n\n")
	
	print("Results of calling simple_add() multiple times with different parameters:")
	print("4 + 5: " + str(simple_add(4, 5)))
	first = 2
	second = 12
	print("2 + 12: " + str(simple_add(first, second)))
	first = first + 1
	second = second / 2
	print("3 + 6: " + str(simple_add(first, second)), end="\n\n")
	
	print("Functions that use parameters can do all sorts of things:")
	print(name_three_part_sandwich("bacon", "lettuce", "tomato"))
	print(name_three_part_sandwich("sausage", "egg", "cheese"))
	print(name_three_part_sandwich("rocks", "ice", "dirt"), end="\n\n")

'''
More complex parameter usage examples:
'''

# What happens if we reassign a parameter? Is the original variable passed in changed?
def reassign_parameter(thing_to_change):
	print("here's the value of thing_to_change before: " + str(thing_to_change))
	thing_to_change = 7
	print("here's the value of thing_to_change after: " +  str(thing_to_change), end="\n\n")
	
# What happens if we sort a list? Will the original list passed in change?
def attempt_to_modify_list(list_to_modify):
	print("Here's the value of list_to_modify before: " + str(list_to_modify))
	list_to_modify.sort()
	print("Here's the value of list_to_modify after: " + str(list_to_modify), end="\n\n")

# What happens if we try to make a string upper case? Will the original string change?
def attempt_to_modify_string(string_to_modify):
	print("Here's the value of string_to_modify before: " + str(string_to_modify))
	string_to_modify.upper()
	print("Here's the value of string_to_modify after: " + str(string_to_modify), end="\n\n")
	
def complex_parameters_example():
	print() 
	
	my_name = "sam"
	print("Original value of my_name: " + my_name, end="\n\n")
	reassign_parameter(my_name)
	print("Final value of my_name: " + my_name, end="\n\n\n")
	
	list_of_names = ["sam", "eve", "alice", "bob"]
	print("Original value of list_of_names: " + str(list_of_names), end="\n\n")
	attempt_to_modify_list(list_of_names)
	print("Final value of list_of_names: " + str(list_of_names), end="\n\n\n")
	
	lower_case_string = "small"
	print("Original value of lower_case_string: " + lower_case_string, end="\n\n")
	attempt_to_modify_string(lower_case_string)
	print("Final value of lower_case_string: " + lower_case_string, end="\n\n\n")

# It's a good idea to keep main() as clean as possible, since it has to hold everything else together.	
def main():
	input("Press enter when you're ready to see the results of basic_paramters_example()")
	basic_parameters_example()
	
	input("Press enter when you're ready to see the results of complex_parameters_example()")
	complex_parameters_example()
	
	print("The examples are all done now. Wasn't that fun?")

if __name__ == "__main__":
    # execute only if run as a script
    main()