"""
In 1937, a German mathematician named Lothar Collatz 
formulated an intriguing hypothesis as shown below

"""
stepCount = int(0)

c0 = int(input("Enter non-negative and non-zero integer number: "))

while (c0 != 1):
    stepCount += 1
    if c0%2 == 0: # if even, divide it by 2, repeat unless it reaches to 1
        c0 //=2
        print(c0)
    else:
        c0 = c0*3+1 # multiply by 3 then add 1, repeat unless it reaches to 1 
        print(c0)

print('Steps:',stepCount)

