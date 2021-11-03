# This is a interesting way to call for LIST and 
# using print to call a function 
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list



print(list_sum([5, 4, 3]))

print(strange_list_fun(5))

# t = [[3 - i for i in range(3)] for j in range(3)]
# the above builds up a LIST inside LIST as shown below
# [[3, 2, 1], [3, 2, 1], [3, 2, 1]]


# Testing out what is going on with the above line part by part
# starting with the inner []

v = [3 - i for i in range(3)] 
print(v)
# the single line created [3, 2, 1]
# the fastest way to create a v and filled with numbers  

print('\n')

# below is the traditional way, which takes 3 lines
t = []
for i in range(1,3):
    t.append(3 - i)

print(t)

# t[0] = 100
# t[1] = 200
# You cannot assign the above way because t is created as
# empty list 
# 
# ## Error message 
# ##     t[0] = 100
# ## IndexError: list assignment index out of range
# 
# # rgr



# my_list = [[0,1,2,3] for i in range(2)]
# print(my_list[2][0])



# my_list = [i for i in range(-1,2)]
# print(my_list)


