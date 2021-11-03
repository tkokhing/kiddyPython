# THIS IS A GOOD SUMMARY ON USAGE OF FOR AND WHILE ELSE LOOPS

# Create a for loop that counts from 0 to 10, and 
# prints odd numbers to the screen. Use the skeleton below:

print('\n Print odd inside 0 to 10 using for loop')
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

print('\n')

# Create a while loop that counts from 0 to 10, and 
# prints odd numbers to the screen. Use the skeleton below:

print('\n Print odd inside 0 to 10 using while loop')
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

print('\n')

# Create a program with a for loop and a break statement. The program 
# should iterate over characters in an email address, 
# exit the loop when it reaches the @ symbol, and 
# print the part before @ on one line. Use the skeleton below:

print('\n')
print('\n Print email head')
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Create a program with a for loop and a continue statement. The program should 
# iterate over a string of digits, replace each 0 with x, and 
# print the modified string to the screen. Use the skeleton below:

print('\n')
print('\n Print x instead of 0 of a string of numbers')
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")


# What is the output of the following code?
print('\n')
print('What is the output numbers?')
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# What is the output of the following code?
print('\n')
print('What is the output numbers?')
n = range(4)  # never knew can be define and run in for loop this way 
for num in n:
    print(num - 1)
else:
    print(num)

# What is the output of the following code?
print('\n')
print('What is the output numbers?')
for i in range(0, 6, 3):
    print(i)