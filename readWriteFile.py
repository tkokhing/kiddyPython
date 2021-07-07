# This is Python for Data Science, Exercise 4-2, by Cognitiveclass.ai 
"""
Your local university's Raptors fan club maintains a register
of its active members on a .txt document. 
Every month they update the file by removing the members who are not active. 
You have been tasked with automating this with your Python skills.
Given the file currentMem, Remove each member with a 'no' in their Active coloumn. 
Keep track of each of the removed members and append them to the exMem file. 
Make sure the format of the original files in preserved. 
(Hint: Do this by reading/writing whole lines and ensuring the header remains )
"""
#Run this prior to starting the exercise. genFiles is by Cognitiveclass.ai
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))

    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

# ********** cleanFiles is to be written, which is by me ********** 
def cleanFiles(currentMem,exMem):
    inActiveMemList = []
    stillActiveMemList = []

    with open(currentMem,'r') as filterNoMem:  # w+ can truncate
        lineByLine = filterNoMem.readline() # flush off the header in the first line
        lineByLine = filterNoMem.readlines() # reads the remaining lines as a List, where each element is a single line entry
        # for looop to read each line (or element)
        for eachLine in lineByLine:
            wordsByList = eachLine.split() # split by words inside each element str 
            if wordsByList[2] == 'no': # if 3 column of element str contains no, copy to inActiveMemList
                inActiveMemList.append(wordsByList)
            else:
                stillActiveMemList.append(wordsByList) # else, copy to stillActiveMemList
            # append and extend, MUST MUST remember the difference
    # my above codes do not content \n unlike the cogitive one, 
    # because I thought it will be a concent but
    # actually not seeing Cognitiveclass sample answer.

    with open(currentMem,'w+') as overWriteFile:
        newListLength = len(stillActiveMemList)

        overWriteFile.write('Membership No  Date Joined  Active  \n')
        dataFmt = "{:^13}  {:<11}  {:<6}\n"
        
        for i in range (newListLength):
            overWriteFile.write(dataFmt.format(stillActiveMemList[i][0],stillActiveMemList[i][1],stillActiveMemList[i][2]))

    with open(exMem,'a') as addOntoFile:
        newListLength = len(inActiveMemList)

        dataFmt = "{:^13}  {:<11}  {:<6}\n"
        addOntoFile.seek(0,2) # move 0 bytes starting at the end.
        for i in range (newListLength):
            addOntoFile.write(dataFmt.format(inActiveMemList[i][0],inActiveMemList[i][1],inActiveMemList[i][2]))

# **********    Above is by me **********
"""
# Comparing with cognitiveclass sample answer, the following are what I have learnt: 
1. Header is just a str, and a few of their lines can be better written - which i did
2. facinating for loop <<inactive = [member for member in members if ('no' in member)]>>
3. Better understanding in using r+, a+ and truncate
4. However, there is a neater way to write but has to modify also the genFiles function   
"""
# run genFiles first, then duplicate each of inactive.txt and members.txt
# these serves as a reference
# turn off genFiles and run cleanFiles
#genFiles(memReg,exReg)
cleanFiles(memReg,exReg)

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())