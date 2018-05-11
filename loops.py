my_variable = "hello, asshole"

# print(my_variable[0]) #prints Index 0 (the letter 'h')
# print(my_variable[1]) #prints Index 0 (the letter 'h')
# print(my_variable[2]) #prints Index 0 (the letter 'h')
# print(my_variable[3]) #prints Index 0 (the letter 'h')
# print(my_variable[4]) #prints Index 0 (the letter 'h')
#but if we increase length of my_variable, we have to add more lines
#so...
for character in my_variable: #iterables are strings, lists, tuples, etc.
    print(character) #"character" can be called anything; is just a "variable"

my_list = [1, 2, 3, 4, 5]
for number in my_list:
    print(number ** 2)

user_wants_number = True
while user_wants_number == True:
    print(10)
    #user_wants_number = False
    user_input = input("Shall we print again? (y/n): ")
    if user_input == 'n':
        user_wants_number = False


