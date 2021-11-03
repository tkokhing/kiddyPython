my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 7]
temp_list =[]
no_dup_list=[]

temp_list=sorted(my_list)
temp_list.append(10000000)

lengthList = len(temp_list)

for i in range (lengthList-1):
    if (temp_list[i])!=(temp_list[i+1]):
        no_dup_list.append(temp_list[i])

print('The sorted no duplicates list is: ', no_dup_list)
temp_list=[]

for numberA in my_list:
    for numberB in no_dup_list:
        print(numberA)
        print(numberB)
        print("\n")
        if numberA==numberB:
            temp_list.append(numberA)

