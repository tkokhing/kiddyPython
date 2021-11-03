# break - example
# break - exits the loop immediately, and unconditionally ends the
#  loop's operation; the program begins to execute the
#  nearest instruction after the loop's body;

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# The break instruction:
# Inside the loop. 1       
# Inside the loop. 2       
# Outside the loop.        


# continue - example 
# continue - behaves as if the program has suddenly 
# reached the end of the body; the next turn is started and 
# the condition expression is tested immediately.

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# The continue instruction:
# Inside the loop. 1       
# Inside the loop. 2       
# Inside the loop. 4       
# Inside the loop. 5       
# Outside the loop.     


# below is a better example for demo break and continue
# below is a better example for demo break and continue
# below is a better example for demo break and continue


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    print(i)
    print(found)
    if found:
        print('Breaking Bad')
        break

if found:
    print("Element found at index", i)
else:
    print("absent")



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

print('\n')
for i in range(len(my_list)):
    found = my_list[i] == to_find
    print(i)
    print(found)
    if found:
        print('Continue to be Bad') # enter here once but continues which i increases ending up as False
        continue

if found:
    print("Element found at index", i)
else:
    print("absent")