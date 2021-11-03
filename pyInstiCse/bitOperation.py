x = 4
# 0000 0100

y = 1
# 0000 0001


a = x & y
# and operation
# 0000 0100
# 0000 0001
# -----------
# 0000 0000

# a = 0 <ans>

b = x | y
# or operation
# 0000 0100
# 0000 0001
# -----------
# 0000 0101

# b = 5 <ans>


c = ~x  # tricky!
# not operation
# 0000 0100
# 1111 1011
# 1 + 2 + 8 + 16 + 32 + 64 + 128  
# c = 251 <ans> !!! wrong. It is 2's complement

"""
HOW TO DO 2's Complement?

Step 1: Invert the bits
Step 2: Add ONE to the bits

For example, using 1 byte (=8 bits), the decimal number 5 is represented by

0000 0101
The most significant bit is 0, so the pattern represents a non-negative value. 
To convert to −5 in two's-complement notation, first, the bits are inverted, that is: 0 becomes 1 and 1 becomes 0:

1111 1010
At this point, the representation is the ones' complement of the decimal value −5. 
To obtain the two's complement, 1 is added to the result, giving:

1111 1011

There are two more methods. Read this
https://en.wikipedia.org/wiki/Two%27s_complement

"""

d = x ^ 5
# 0000 0100 , x
# 0000 0101 , 5
# ==========
# 0000 0001 , 1 <ans>


e = x >> 2
# 0000 0100
# 0000 0001

# e = 1 <ans>

f = x << 2
# 0000 0100
# 0001 0000

# f = 16 <ans>

#  0 , 5 ,  251 , 1  ,  1 , 16

print(a, b, c, d, e, f)
#  0 , 5 ,  -5 , 1  ,  1 , 16
