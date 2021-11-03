#
# This is tested good to part 4. Dictionary attack
# 
# 

import hashlib

# sample codes provided by Anila
# hashed = hashlib.md5("password".encode()).hexdigest()
# print(hashed)
# print(len(hashed))

wordList = []

#   <<<  TRIAL TEST 1 >>> 
# dummy-hash5.txt is reverse-engineered hash created from the randomly 
# picked words from words5.txt - It is then tested successfully 
# i.e. able to return matches of hashes
#with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/dummy-hash5.txt','r') as File1:

#   <<<  TRIAL TEST 2 >>> 
# When tested with the given <studentID-hash5.txt>, no result ==> Thus, 
# the contains no hashed from list of words inside word5.txt 
# with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/1006592-hash5.txt','r') as File1:

with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/dummy-hash5.txt','r') as File1:
    FileContent = File1.readlines()
    for line in FileContent:
        cleanLine = line
        eachHash = cleanLine.split()
        wordList.extend(eachHash)

wordLength = len(wordList)

#   print(wordList) # make sure contains are copied to wordList
#   print(type(wordList[i])) # confirmed that type as str
#   print('\n')

with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/words5.txt','r') as word5clue:
    FileContent = word5clue.readlines()
    for line in FileContent:
        hashed = hashlib.md5(line.encode()).hexdigest()
        
        for i in range (0,wordLength):
            if wordList[i] == hashed:
                print('\n', wordList[i])
                print(i,'Match found for word: ', line, 'with its hash : ', hashed)
            # else:
            #     print(i,'No matches found for word: ', line, 'with its hash : ', hashed)
print(' End of search')