# TEST 3 - tricky questions, strange ways of using the codes but it is a good test 
# It covers Module 3 - Boolean values, 
# conditional execution, loops, lists and list processing, 
# logical and bitwise operationsExternal tool

# a = 1
# b = 0
# c = a & b
# d = a|b
# e = a^b
# print (c + d + e) 


# my_list = [[0,1,2,3] for i in range(2)]
# print(my_list[2][0])



# my_list = [i for i in range(-1,2)]
# print(my_list)

# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])


# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])


# my_list1 = [1, 2, 3]
# my_list2 = []

# for v in my_list1:
#     print(v)
#     my_list2.insert(0,v)

# # insert in my_list2[0] with 1
# # insert in my_list2[0] with 2, in turn pushes 1 to my_list2[1] 
# # insert in my_list2[0] with 3, in turn pushes 1 to my_list2[2] and 2 to my_list2[1]
# # 3 will be at my_list2[0] 
# print(my_list2)



# for i in range(1):
#     print('ha')
# else:
#     print('la')



# nums = [1, 2, 3]
# vals = nums[-1:-2]
#   # vals = nums[-2:-1] 
#   # this gives error
# print(vals)



# nums = [1, 2, 3]
# for v in range (len(nums)):
#     nums.insert(1,nums[v]) # the next time you enter, the list is actually updated already and taking the new list
#     print(v)
#     print(nums)
# print('\n')
# print(nums)



# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(vals)



# i = 0
# while i <= 5:
#     i += 1
#     if i%2==0:    # damn... obviously the first time is hit remainder = 0 which is i =2, it will break
#         #print(i)
#         break
        
#     print('#')
#     #print(i)



# i = 0
# while i < 6:
#     i += 1
#     if i%2==0:    # damn... obviously the first time is hit remainder = 0 which is i =2, it will break
#         #print(i)
#         continue
        
#     print('\n#')
#     print(i)



# vals = [0, 1 , 2]
# vals.insert(0,1)
# del vals[1]
# print(vals)
# print(sum(vals))



# t = [[3 - i for i in range(3)] for j in range(3)]
# # the above builds up a LIST inside LIST as shown below
# # [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
# s = 0
# print(t)
# for i in range (5):
#     s += t[i][i]

# print('Sum s: ',s)

# # # # my own testing
# # # # my own testing
# # # # my own testing
# t = [[3 - i for i in range(3)] for j in range(5)]
# # the above builds up a LIST inside LIST as shown below
# # # [[3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 1], [3, 2, 1]]

# for i in range (5):
#     print(t[i][0])
# #   3
# #   3
# #   3
# #   3
# #   3

# print(t[4][2])
# #   1


# t = [[3 - i for i in range(3)] for j in range(3)]
# the above builds up a LIST inside LIST as shown below
# [[3, 2, 1], [3, 2, 1], [3, 2, 1]]


# Testing out what is going on with the above line part by part
# starting with the inner []

v = [3 - i for i in range(3)] 
print(v)
# the single line created [3, 2, 1]

print('\n')

# below is the traditional way, 3 lines
t = []
for i in range(0,3):
    t.append(3 - i)
        
print(t)

# my_list = [[0,1,2,3] for i in range(2)]
# print(my_list[2][0])



# my_list = [i for i in range(-1,2)]
# print(my_list)