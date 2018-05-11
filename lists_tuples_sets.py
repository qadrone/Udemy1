my_variable = "hello"

# grade_A = 100
# grade_B = 90
# grade_C = 80
# grade_D = 70
# grade_F = 60
#
# print((grade_A + grade_B + grade_C + grade_D + grade_F) / 5)

grades = [100, 90, 80, 70, 60, 50] #list, can always change/add/remove
tuple_grades = (100, 90, 80, 70, 60, 50) #tuples are "immutable"..."safer"
set_grades = {100, 100, 77, 89, 43} #unique and unordered

print(set_grades)
grades.append(40) #just adds something to the END of the list
print(sum(grades) / len(grades))
print(grades)
tuple_grades = tuple_grades + (40, ) #has to have a comma
print(tuple_grades)
print(grades[0]) #prints Index 0 of List
print((my_variable) + ", asshole")

# Set Operations
## Which elements are in the set?
lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}
print(lottery_numbers.intersection(winning_numbers)) #items that exist in both sets
print(lottery_numbers.union(winning_numbers)) #no duplicates
print({1, 2, 3, 4}.difference({1, 2}))

my_list = [10, 20, 70]
my_tuple = (50,) #() are for math and are NOT necessary!  Need the comma.
# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
print(set1.intersection(set2))