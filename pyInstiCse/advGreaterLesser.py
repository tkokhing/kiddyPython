print('\nSelf test 1')
x = 5
y = 10
z = 8

print(x > y)
print(y > z)

##############
print('\nSelf test 2')
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

print('\nSelf test 3')
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

##############
print('\nSelf test 4')

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

##############
print('\nSelf test 5')
x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

##############
print('\nSelf test 6')
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

