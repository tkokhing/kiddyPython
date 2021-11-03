import random
import string
import hashlib
import timeit as tm


def dictAttack():
    start = tm.default_timer()
    wordList = []
    messageToWrite = []
    fileMessage = 'Words found using provided Dictionary \n'
    foundHashCounter = 0
    #   <<<  TRIAL TEST 1 >>> 
    # dummy-hash5.txt is reverse-engineered hash created from the randomly 
    # picked words from words5.txt - It is then tested successfully 
    # i.e. able to return matches of hashes
    #with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/dummy-hash5.txt','r') as File1:

    #   <<<  TRIAL TEST 2 >>> 
    # When tested with the given <studentID-hash5.txt>, no result ==> Thus, 
    # the contains no hashed from list of words inside word5.txt 
    # with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/dummy-hash5.txt','r') as File1:
    # Similar small bite tests are done on the 3 others functions/methods

    with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/1006592-hash5.txt','r') as File1:
        FileContent = File1.readlines()
        for line in FileContent:
            eachHash = line.split()
            wordList.extend(eachHash)

    wordLength = len(wordList)    

    with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/words5.txt','r') as word5clue:
        FileContent = word5clue.readlines()
        for line in FileContent:
            hashed = hashlib.md5(line.encode()).hexdigest()
            
            for i in range (0,wordLength):
                if wordList[i] == hashed:
                    print('\n', wordList[i])
                    print(i,'Match found for word: ', line, 'with its hash : ', hashed)
                    foundWord = 'Matched word:' + line + '==>' + 'Hash: ' + hashed
                    messageToWrite.append(foundWord)
                    foundHashCounter += 1

    end = tm.default_timer()

    timeTaken = 'Time taken is: ' + str(end - start) + ' for [' +str(foundHashCounter) + '] out of ' + str(wordLength) + ' found.'
    
    outputFile('DictAttack.txt',fileMessage, messageToWrite, timeTaken)    

def bruteLowerCase():
    start = tm.default_timer()
    charList = 'abcdefg' # tester only
    # charList = 'abcdefghijklmnopqrstuvwxyz'
    len_charList = len(charList)
    wordList = []
    messageToWrite = []
    fileMessage = 'Words found using Bruteforce with lowercase \n'
    foundHashCounter = 0

    #with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/1006592-hash5.txt','r') as File1:
    with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/dummy-hash5.txt','r') as File1: # tester only
        FileContent = File1.readlines()
        for line in FileContent:
            eachHash = line.split()
            wordList.extend(eachHash)

    wordLength = len(wordList)

    for i in range (0,len_charList):
        for j in range (0,len_charList):
            for k in range (0,len_charList):
                for l in range (0,len_charList):
                    for m in range (0,len_charList):
                        dictWord = str(charList[i]) + str(charList[j]) + str(charList[k]) + str(charList[l]) + str(charList[m])
                        hashed = hashlib.md5(dictWord.encode()).hexdigest()
                        print(dictWord,':' , hashed)
                        
                        for q in range (0,wordLength):
                            if wordList[q] == hashed:
                                foundWord = 'Matched word:' + dictWord + '==>' + 'Hash: ' + hashed
                                messageToWrite.append(foundWord)
                                foundHashCounter += 1

    end = tm.default_timer()

    timeTaken = 'Time taken is: ' + str(end - start) + ' for [' +str(foundHashCounter) + '] out of ' + str(wordLength) + ' found.'
    
    outputFile('BruteLowerCase.txt',fileMessage, messageToWrite, timeTaken)    


def bruteLowerCaseDigit():
    start = tm.default_timer()
    charList = 'abcd123' # tester only
    # charList = 'abcdefghijklmnopqrstuvwxyz1234567890'
    len_charList = len(charList)
    wordList = []
    messageToWrite = []
    fileMessage = 'Words found using Bruteforce with lowercase and digits \n'
    foundHashCounter = 0
    
    #with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/1006592-hash5.txt','r') as File1:
    with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/dummy-hash5.txt','r') as File1: # tester only
        FileContent = File1.readlines()
        for line in FileContent:
            eachHash = line.split()
            wordList.extend(eachHash)

    wordLength = len(wordList)

    for i in range (0,len_charList):
        for j in range (0,len_charList):
            for k in range (0,len_charList):
                for l in range (0,len_charList):
                    for m in range (0,len_charList):
                        dictWord = str(charList[i]) + str(charList[j]) + str(charList[k]) + str(charList[l]) + str(charList[m])
                        hashed = hashlib.md5(dictWord.encode()).hexdigest()
                        print(dictWord,':' , hashed)
                        
                        for q in range (0,wordLength):
                            if wordList[q] == hashed:
                                foundWord = 'Matched word:' + dictWord + '==>' + 'Hash: ' + hashed
                                messageToWrite.append(foundWord)
                                foundHashCounter += 1

    end = tm.default_timer()

    timeTaken = 'Time taken is: ' + str(end - start) + ' for [' +str(foundHashCounter) + '] out of ' + str(wordLength) + ' found.'

    outputFile('BruteLowerCaseDigit.txt',fileMessage, messageToWrite, timeTaken)    


# def addSaltNewPword(length):

    # start = tm.default_timer()
    # wordList = []
    # fileMessage = 'Salted added \n'
    # foundHashCounter = 0
    
    # with open('D:/TKH/10_MSSD/10.3_T1/51.506 STL1/STL1-W1/15hash5.txt','r') as File1: # tester only
    #     FileContent = File1.readlines()
    #     for line in FileContent:
    #         eachHash = line.split()
    #         letters = string.ascii_lowercase
    #         saltStr = ''.join(random.choice(letters) for i in range(length))
    #         eachHash = eachHash + saltStr
    #         wordList.extend(eachHash)
    
    # # wordLength = len(wordList)

    # #                     for q in range (0,wordLength):
    # #                         if wordList[q] == hashed:
    # #                             foundWord = 'Matched word:' + dictWord + '==>' + 'Hash: ' + hashed
    # #                             messageToWrite.append(foundWord)
    # #                             foundHashCounter += 1


    # end = tm.default_timer()

    # timeTaken = 'Time taken is: ' + str(end - start) + ' for [' +str(foundHashCounter) + '] out of ' + str(wordLength) + ' found.'

    # outputFile('hash6.txt',fileMessage, messageToWrite, timeTaken)    


def outputFile(fileName, header, message,timeTaken):
    saveFile = open(fileName,'w')
    saveFile.write(header)
    messageLength = len(message)
    i = 0 
    while (i != messageLength):
        sentence = str((message[i]) +'\n')
        saveFile.write(sentence)
        i += 1
    saveFile.write(timeTaken)
    saveFile.close()

def main():
    thissessionLogIn = True
    
    while thissessionLogIn == True:
        print('\n')
        print('===================================================','\n')
        print('\t','[1] - Dictionary Attack')
        print('\t','[2] - Bruteforce with only lowercase')
        print('\t','[3] - Bruteforce with only lowercase and digits')
        print('\t','[4] - Add Salt and make New password')
        print('\t','[0] - Exit','\n')
        sessionInput=input('Please choose? (Enter a number) ')

        if sessionInput == '1':
            print('File [DictAttack.txt] will be generated, please wait')
            dictAttack()

        elif sessionInput == '2':
            print('File [BruteLowerCase.txt] will be generated, please wait')
            bruteLowerCase()
        
        elif sessionInput == '3':
            print('File [BruteLowerCaseDigit.txt] will be generated, please wait')
            bruteLowerCaseDigit()

        elif sessionInput == '4':
            print('You have enter 4')
            #addSaltNewPword(1)

        elif sessionInput == '0':
            print('You have enter 0')
            # sessionLogIn = 1
            thissessionLogIn = False
 
        else:
            print('Please enter a correct option')


main()
print('Thank you SUTD for the opportunity')
input()
