entered_word = input('Enter any word: ')

user_word = entered_word.upper()

for letter in user_word:
    #if letter == 'A' or 'E' or 'I' or 'O' or 'U':
    # elif letter == 'I' or 'O' or 'U':
    #     continue
    # do not understand why or does not work

    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
 
    print(letter)

# while and else 

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# 1      
# 2      
# 3      
# 4      
# else: 5 // increased to 5 because of the +=1 inside the while loop

for i in range(5):
    print(i)
else:
    print("else:", i)

# 0
# 1
# 2
# 3
# 4
# else: 4 // will not incr to 5 because the range limits to max 4 inclusive
