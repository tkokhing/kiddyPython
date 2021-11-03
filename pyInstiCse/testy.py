# print(chr(110))

a = [1, 2, 3]
b = [4, 5, 6]
#c = []

'''
def add_two(a, b):
    c = []
    # print(a)
    # print(b)
    # print(len(a))
    # print(len(b))
    for number in range (0,len(a)):
        #print(number)
        print(~a[number]+1)
        #print(~a[number]|1)
        print(~b[number]+1)
        #print(~b[number]|1)
        c.append(((~a[number]+1)^(~b[number]+1)) +2)
    
    return c
'''
def dot_two(a, b):
    c = 0
    print(a)
    print(b)
    print(len(a))
    print(len(b))
    for number in range (0,len(a)):
        #print(number)
        print(a[number])
        print(b[number])
        c = c + (a[number]*b[number])
    
    return c



print(dot_two(a, b))

#print(add_two(a, b))
# print(a+10*b)