# VARIABLES
a = 5
my_variable = 56
my_10_variable = 1
# 10variable = Nope, can't do this
# these are variables: a box with something in it
# we are "defining" a variable

string_variable = "hell0"  # set of characters is a String
string_quotes = 'strings can have single quotes'  # no diff btw single/double quotes
# pick one and stick with it

print(my_variable)  # "print" is a METHOD which outputs variable to console
print(string_variable)
# print("hello, world")
# print(123)

# first quiz
var1 = "test"
var2 = "test"


# num1 = 8
# num2 = 2

# print(num1 * num2)

# METHODS (should always be Actions, such as "print")
# define a new method
def my_print_method(my_parameter):  # parameter/argument same thing
    print(my_parameter)


# my_print_method() #this is to RUN the method - expects an argument
my_print_method("hello, world!")  # "my_paramenter" now = "hello, world!"


def my_multiply_method(num_one, num_two):
    return num_one * num_two


result = my_multiply_method(5, 3)
# print(result) (option 1)
my_print_method(result)  # (option 2)
# the above are more "readable" than below

# my_print_method(my_multiply_method(5, 3))
