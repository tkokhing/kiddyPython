#Run this prior to starting the exercise
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

# this is by cogitive class ##
# =============================== #
def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            #            header = members[0]
            #            members.pop(0)
            # above 2 lines by Cognitive can be written as 1 as corrected below
            header = members.pop(0)

            inactive = [member for member in members if ('no' in member)]
           
            # ----------------------------
            #  The above is the same as 

            #  for member in active:
            #  if 'no' in member:
            #      inactive.append(member)
            # ----------------------------
            ### below is trying to understand how testing of 'no' can work
            # >>> coz I thought written in columns of txt file will be tab, 
            # aka str within list. So the truth is it is str by str
#            print(type(inactive))
#            print(type(inactive[4]))
#            print(inactive[4])
#            len_4 = len(inactive[4])
#            print('Length of 4 is: ',len_4)
#            for i in range (len_4):
#                print('>>',i,'==',inactive[4][i])
#            print('last letter',inactive[5][-1],'is between')

            #go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header) # write back the header that was pop back as the header of the updated Active Mem file
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()

# By printing inactive, the output is 
# ['    92615      2019-1-8     no    \n', 
# '    35476      2017-9-9     no    \n', 
# '    96166      2016-6-14    no    \n', ... ]
# 
# There is \n. interestingly by print inactive[x], the \n does not appears
# But it is there at index 34. index 0 - 33 are occupied by characters. 
# This will serve as inputting a new line with written/transferring to another file 
# There are no tabs in between the string as tested in the notepad
#     
# Above is from cogitiveclass
# ###

# Below lien is by Cog, but there is no meaning and not used at all
# headers = "Membership No  Date Joined  Active  \n"

# Run genFiles first, while turn off cleanFiles, duplicate each of inactive.txt and members.txt as reference
# turn off genFiles, run cleanFiles. Compare the results which the duplicated copies

#genFiles(memReg,exReg)
cleanFiles(memReg,exReg)

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())    