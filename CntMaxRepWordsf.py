# Count the number of words in a txt file
# Group and determine the top 3 most recurring words and their counts of a txt file
# txt file (Google.txt) content is extracted from: https://support.google.com/a/answer/7053530
# At line 28, replace the txt file accordingly to run this code
'''
readMyFile = open('C:/Users/timma/OneDrive/Desktop/Computer Related/Google.txt','r').read()
print('\n','This is reading filename Google.txt without splitting')
print('\n')
print('==================================')
print(readMyFile)
# print(readMyFile.name)
# print(readMyFile.mode)
'''

wordList = []
repeatedWordList = []
wordCountList = []
maxWordList = []
# intially created it as maxWordList = ['',''] thinking that it will meant 
# as pairing of list. However it does not need to define the pairing
# it also created ['',''] at the end of the maxWordList which is unwanted 
# The ['',''] also jammed sorting with 
# the TypeError: '<' not supported between instances of 'str' and 'list'

i = int(0)
print('\n')
print('==================================')
with open('C:/Users/timma/OneDrive/Desktop/Computer Related/Google.txt','r') as File1:
    FileContent = File1.readlines()
    for line in FileContent:
        cleanLine = line.replace('.','').replace('!','').replace('?','').replace(',','').replace(';','').replace(':','')
        #print('>>>',line,'<<<')
        #for word in line:
        eachWord = cleanLine.split()
        print('\n')
        print(i,'>>>',eachWord,'<<<')
        wordList.extend(eachWord)
        i += 1
        #print(FileContent)
        #print(FileContent[i])
    # print(FileContent)
sorted_wordList = sorted(wordList)
print('========= Sorted_wordList ========')
print(sorted_wordList)
print('==================================')

listLength = len(sorted_wordList)
print(listLength)
for i in range (0,listLength):
    print(sorted_wordList[i])

# add a fake and impossible word so that the for loop 
# will run to the real end sortedWordList  
sorted_wordList.append('ZZZZZZZZXYYZZ')


wordCounter = 1
repeatedWordCounter = 0 

for i in range (0,listLength):
    # repeated words found
    if sorted_wordList[i] == sorted_wordList[i+1]:
        print('Repeated words', sorted_wordList[i])
        # if that word is not inside repeatedWordList,
        # it is the first occurrance 
        # write word into repeatedWordList
        # start counting repeatedWordCounter for indexing List purpose
        # add 1 to wordCounter
        if sorted_wordList[i] not in repeatedWordList:
            repeatedWordList.append(sorted_wordList[i])
            repeatedWordCounter += 1
            wordCounter += 1
      
        # if that word is already inside repeatedWordList, 
        # add wordCounter
        else:
            wordCounter += 1
            
    # End of repeated words, or start of new word
    else: 
        # if there are already same words found
        # write to total count of the same word into wordCoutlist [] 
        # at position by repeatedWordCounter
        # once written, reset wordCounter to 1 for next use
        if wordCounter >= 2: 
            wordCountList.insert(repeatedWordCounter, wordCounter)
            wordCounter = 1

        # sequence of single word, reset wordCounter to prepare for new repeated words
        else: 
            wordCounter = 1

for x in range (0,repeatedWordCounter):
    maxWordList.insert(x,[wordCountList[x],repeatedWordList[x]]) 



print('The last word in sortedWordList is: ',sorted_wordList[-1])
print('\n','The repeatedWorkList: ', repeatedWordList)
print('\n','The wordCountList: ', wordCountList)
print('\n','The repeatedWordCounter is: ', repeatedWordCounter)
print('\n','The last wordCounter is: ', wordCounter)
print('\n','The maxWordList is: ', maxWordList)

maxWordList.sort(reverse=True)

print('The top 3 repeating words are:')
for i in range (0,3):
    print(maxWordList[i][1], ':', maxWordList[i][0], 'times')



"""
print('==================================')
print('File type of File1: ',type(File1))
print('File type of FileContent: ',type(FileContent))
print('File type of line: ',type(line))
print('File type of eachWord: ',type(eachWord))
print('File type of maxWordList is: ', type(maxWordList))
print('\n','The repeatedWorkList: ', type(repeatedWordList))
print('\n','The wordCountList: ', type(wordCountList))
print('\n','The 5th repeatedWorkList: ', type(repeatedWordList[5]))
print('\n','The 5th wordCountList: ', type(wordCountList[5]))

#==== Below is the output of the above ====
#==== They are what I expected!!! ====

File type of File1:  <class '_io.TextIOWrapper'>
File type of FileContent:  <class 'list'>
File type of line:  <class 'str'>
File type of eachWord:  <class 'list'>
File type of maxWordList is:  <class 'list'>

The repeatedWorkList:  <class 'list'>

The wordCountList:  <class 'list'>

The 5th repeatedWorkList:  <class 'str'>

The 5th wordCountList:  <class 'int'>

print('==================================')

if File1.closed == True:
    print('==================================')
    print('File is closed')
    print('==================================')


if FileContent == False:
    print('File content has flushed.')
else:
    print(' with open is great, even file is closed')
    print('File content is still available to print as shown:')
    print('==================================')
    # print(FileContent)
    print('==================================')

append joins the 2 Lists into one into Dict
[['ListA1','ListA2], ['ListB1','ListB2']]

extend combines as one list
['ListA1','ListA2,'ListB1','ListB2']
"""