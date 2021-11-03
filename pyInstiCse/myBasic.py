# Literals. Something not share in any other training materials 

# Literals are notations for representing some fixed values in code. 
# Python has various types of literals - for example, 
# a literal can be a number (numeric literals, e.g., 123), 
# or a string (string literals, e.g., "I am a literal."). 

# In Python only, this 0o123 [Zero-o or Zero-O] represents a Octal number
# Big or small O does not make any difference
# Max is till 7. I.e. there is no 0o108. Python will give error  
print(0o100)

# Only in Python, this 0x123 [Zero-x or Zero-X] rep hexadecimal numbers.
# Max is till F which equals to 15. I.e. there is no 0o108. Python will give error  
print(0x020)
print(0xF20)

# 3 times ten to the power of 8
# which is what commonly written as 3X10^8 mathematically 
# But, in Python (and most scientific calculator) it is written as 3E8 or 3e8, where E is exponent 
# the exponent (the value after the E) has to be an integer;
# the base (the value in front of the E) may be an integer.

# Planck's constant (and denoted as h), according to the textbooks, 
# has the value of: 6.62607 x 10^34. 
# So Python is 6.62607E-34. 
# To sum up, Python always chooses the more economical form of the 
# number's presentation, and you should take 
# this into consideration when creating literals.

# Recall how it is derive using hardcore basic mathematics

# 0x00F
# (0 x 256) + (0 X 16) + (15 x 1) = 15

# 0x0FF
# (0 x 256) + (15 X 16) + (15 x 1) = 255

# 0x0FF + 0x001 = 0x100 = 255 + 1 = 256 

# 0x100
# (1 x 256) + (0 X 16) + (0 x 1) = 256

# Mathematically, it is...
# (0 x {16^2}) + (0 X {16^1}) + (0 x {16^0})


# Floor division, 3//2 ==> chop off decimal point
# Exponent, 3**2 ==> 3^2 giving you 9
# Modulas, 100%2 ==> finding the reminder after dividing, but it is
# usual used to determine if a number is even or odd. 

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print('\n')

# when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print('\n')

print(12 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# The result produced by the division operator is ALWAYS a float, 
print(6 // 3) 
# chop off decimals. This will get an interger as answer PROVIDED both are intergers

# / operator returns a float but what is behind the decimal places???
print('Try examples that are NOT neatly dividable like 6 divided by 3')
print(7.7 // 3)
print(7 // 3.7)
print(7 // 3.)
print(7. // 3)
print(7. // 3.)
print('\n')
print('When either one is float, the Floor division will returns in Float Type but,\
    it is always x.0  ... zeros behind the decimal place.')
print(7 // 3)
print(6 // 3) 
print('When both are integer, the Floor division will returns in Int Type and,\
    without any decimal -  rounding DOWN to the nearest integer value')
# when either one is float, the Floor division will returns in Float Type but, 
# it is always x.0  ... zeros behind the decimal place. 
x = 7 // 3
y = 7. // 3
print(type(x))
print(type(y))
print('\n')

print('Play with negative to appreciates ROUNDING DOWN to the nearest integer')
print(7.7 // 3) 
print(-7.7 // 3)
print(7 // 3)
print(-7 // 3)

print(12 % 5)
print(12 % 5.0)
print(12.0 % 5.0)
print(12.0 % 5)

print(12 % 4.5)
print(-12 % 4.5)
print(12 % -4.5)

"""
3.0
1.5
-1.5

Go back to basics
12/4.5 = 2.666...  <<real answer>>
12//4.5 = 2.0 <<round down>>
-12//4.5 = -3.0 <<round down>>
12//-4.5 = -3.0 <<round down>>

print(12 % 4.5)
(the GOLDEN rule still works: 12 // 4.5 gives 2.0; 2.0 * 4.5 gives 9.0; 12 - 9.0 gives 3.0)

print(-12 % 4.5)
(the GOLDEN rule still works: 12 // 4.5 gives <-3.0>; <-3.0> * 4.5 gives <-13.5>; <-12> - <-13.5> gives 1.5)

print(12 % -4.5)
(the GOLDEN rule still works: 12 // -4.5 gives <-3.0>; <-3.0> * <-4.5> gives <13.5>; 12 - <13.5> gives -1.5)

Awesome maths!
"""

# Binding of the operator determines the order of computations 
# performed by some operators with equal priority, put side by side in one expression.
# Most of Python's operators have left-sided binding, with some exception
print(9 % 6 % 2)
# left to right for the above
print(2 ** 2 ** 3)
# right to left

print((2 ** 4), (2 * 4.), (2 * 4))

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

print((2 % -4), (2 % 4), (2 ** 3 ** 2))

print(2//-4)

print(123 + 0.0)

'''

x = float(input("Enter value for x: "))

y = ((x**3)+(2*x))/((x**4)+(3*x*x) + 1)

print("y =", y)
'''