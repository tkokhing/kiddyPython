# Swapping and comparing
# Different ways of using List, integreting with for loops

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

# above is C++ days of swapping
# Python has a sleak one
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1 

########

my_list = [10, 1, 8, 3, 5, 11]
length = len(my_list)
print(length//2)
# this trick works regardless of even or odd length
# i (max half of length) serves as a mid point
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
# [11, 5, 3, 8, 1, 10]



# Copying the entire list.
list_1 = [1]
list_2 = list_1[:] # this is called slice, something not taught by Shrafer
# Shrafer did says that two lists equating only meant that they are pointing to the same memory location 
# He overcame it by having a third party
# Python Insti showed another way called slice [:] as shown above

list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# you can also put in range to slice, e.g. [start:end]. As usual, end is always end-1
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# If the start specifies an element lying further than 
# the one described by the end (from the list's beginning point of view), 
# the slice will be empty:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list) # output is []

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list) # [10, 8, 6]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) # [4, 2]


# Below shows three samples of finding the largest number using slice in LIST

# Sample 1 (Beginner)
my_list = [17, 3, 11, 55, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


# Sample 2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:   # neater way of coding for loops with  "in range"
    if i > largest:
        largest = i

print(largest)

# Sample 3
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:   # slice off index 0 since already used as starter to compare
    if i > largest:
        largest = i

print(largest)
# Sample 3


# Above also uses    <in>   or   <not in>    operators
# this is something I thought it
# <in> is always peg together with for loops only, but not true

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

