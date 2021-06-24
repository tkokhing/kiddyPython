# This is based on on-line lecture and drafted this

import statistics as stat

stuDict = {'Tom':[98,75,74,73,72,71],'Albert':[100,100],'Cathy':[90],'David':[80,74],'Elloit':[70,89]} 
tempStuDict = []

def logInSession():
    validSession = False

    print('Welcome to World Best High School Admin Portal','\n')

    # counter for max 3 attempts for logging ID and PW
    logInIDCheck = 1
    logInPWCheck = 1

    # validity status for ID and PW
    validuserID = False
    validuserPW = False

    while logInIDCheck < 4:
        userID=input('Please enter user ID: ')
        
        if userID == 'Python':
            print('User ID correct')
            logInIDCheck = 4   
            validuserID = True
            while logInPWCheck < 4:
                userPW=input('Please enter user password: ')
                if userPW =='999':
                    print('Password correct')
                    validuserPW = True
                    logInPWCheck = 4
                else:
                    if logInPWCheck == 1:
                        print('Your user password is incorrect, please re-enter user ID','\n')
                        logInPWCheck +=1
                    elif logInPWCheck == 2:
                        print('Second attempt. Your user password is incorrect, please re-enter user ID','\n')
                        logInPWCheck +=1
                    elif logInPWCheck == 3:
                        print('Your user password is incorrect. All 3 attempts used.','\n')    
                        logInPWCheck +=1

        else:
            if logInIDCheck == 1:
                print('Your user ID does not exist or incorrect, please re-enter user ID','\n')
                logInIDCheck += 1
            elif logInIDCheck == 2:
                print('Second attempt. Your user ID does not exist or incorrect, please re-enter user ID','\n')
                logInIDCheck += 1
            elif logInIDCheck == 3:
                print('Your user ID does not exist or incorrect. All 3 attempts used.','\n')
                logInIDCheck += 1
                
    if validuserID == False or validuserPW == False:
        validSession = False
        print('Three attempts failed. Exiting program','\n')
        input()
    else:
        print('Logging in now...')
        validSession = True
    
    return validSession, userID

def main(userID):
    #while sessionLogIn < 1:
    thissessionLogIn = True
    
    while thissessionLogIn == True:
    # how to print long list of items?? print(    )
        print('===================================================','\n')
        print('===================================================','\n')
        print('\t','Hello ',userID)
        print('\t','Welome to World Best High School','\n')
        print('\t','[1] - Enter Grades')
        print('\t','[2] - Remove Students')
        print('\t','[3] - Student Average Grades')
        print('\t','[4] - Exit','\n')

        sessionInput=input('What would you like to do today? (Enter a number) ')

        if sessionInput == '1':
            print('You have enter 1')
            enterGrade()

        elif sessionInput == '2':
            print('You have enter 2')
            removeStu()
        
        elif sessionInput == '3':
            print('You have enter 3')
            studentAvg()
        
        elif sessionInput == '4':
            print('You have enter 4')
            # sessionLogIn = 1
            thissessionLogIn = False
            print('Goodbye')
            # exit()
            # exit () will ask if you want to kill a running program as demo in IDLE. 
            # It however did not show in VS Code. 
            # Since my programs works to exit (end of the program), 
            # i will not be adding this line coz I do not know what which IDE others will use

        else:
            print('Please enter a correct option')

def enterGrade():
    print('===========================================================','\n')
    print('You are now in Enter Grades Menu, please follow the prompt','\n')
    print('There are',len(stuDict),'existing students in this cohort. Their details are as shown:')
    for i in stuDict:
        #if (stuDict[i] == nameStu):
        print('\t','Student Name [',i,'], Grades:', stuDict[i],'\n')

# GOSH, enlightenment, they are: 
# GOSH, enlightenment, they are: 
# GOSH, enlightenment, they are: 
# inside a for loop, the counter, i,  turns out
# to be index which is name of students (Tom, Albert, Cathy,...) and not 1, 2, 3...
# stuDict[i] actually prints out [XX, YY]

    nameStu = input('Enter the student\'s name: ')
    print(type(nameStu))

    gradeStu = input('Enter the student\'s grades: ')
    print(type(gradeStu))
    print('Uploading the grades now...')
    
    recordExist = 0
    # if name does not exist, below line will return error
    # recordExist = len(stuDict[nameStu])

    for i in stuDict:
        if (i == nameStu):
            print('You have entered: ',i,'\n')
            print(i,'records found and grades as shown:',stuDict[i],'\n')
            
            # I am keeping this tempStuDict, compared to below new student, 
            # so that to different methods of calling / adding List[] 
            tempStuDict = int(gradeStu)
            stuDict[i].append(tempStuDict)
            # below is my method but later found append as shown above
            # stuDict[i] = stuDict[i] + [tempStuDict]
            recordExist += 1
            
    if (recordExist == 0):
        print('You have entered a new student [',nameStu,'],', 'records has been added as shown:')
        
        #stuDict[nameStu]=gradeStu
        # above step is definitely cannot, 
        # because gradeStu is not in List[] format
 
        # tempStuDict = int(gradeStu)
        # stuDict[nameStu] = [tempStuDict]
        # above step is KEY!!!  otherwise gradeStu will be treated as str
        # or better still, simplify into one line code below
                
        stuDict[nameStu] = [int(gradeStu)]        
        print('Name: ',nameStu, 'results entered is: ',stuDict[nameStu])
        recordExist += 1
    
    print('\n','The updated records are as shown:','\n')
    
    for i in stuDict:
        print('\t','Student Name [',i,'], Grades :', stuDict[i],'\n')
             
# cannot add 1 to current len of index, and write a value to it, 
# it does not work this way. 
# Either a form of append or extend is needed 

def removeStu():
    print('===========================================','\n')
    print('You are now in the remove student menu')
    print('There are',len(stuDict),'existing students in this cohort. Their details are as shown:')
    for i in stuDict:
        #if (stuDict[i] == nameStu):
        print('\t','Student Name [',i,'], Grades:', stuDict[i],'\n')

    remStu = input('Which student do you want to remove from the school? ')
    
    ##############

    recordExist = 0
    toDelete = 0
    # if name does not exist, below line will return error
    # recordExist = len(stuDict[nameStu])

    for i in stuDict:
        if (i == remStu):
            print('You have entered: ',i,'\n')
            print(i,'records found and grades as shown:',stuDict[i],'\n')
                       
            # confirmDel = input('Please confirm if you want to delete [', remStu, ']: Y / N?')
            # Wanted to display name along with the confirm delete, however 
            # the above line cannot because input cannot take more than 1 parameters
            confirmDel = input('Please confirm if you want to delete [Y / N]')
            #answer = confirmDel.upper()
            if (confirmDel.upper() == 'Y'):
                recordExist += 1
                toDelete += 1
            else:
                print('No amendment to records')
                recordExist += 1

    # why this toDelete is needed outside the confirmation Y? 
    # the reason is that you delete the stuDict while you are still inside the for loop  
    if (toDelete == 1):
        del stuDict[remStu]
        print('\n','The updated records are as shown:','\n')
        for j in stuDict:
            print('\t','Student Name [',j,'], Grades :', stuDict[j],'\n')


    if (recordExist == 0):
        print('You have entered a invalid student name [',remStu,']')
        recordExist += 1
    ##############
    input('Hit ENTER to go back to MAIN MENU') 
    
def studentAvg():
    print('===========================================','\n')
    print('You are now in the finding average score of student menu')
    print('There are',len(stuDict),'existing students in this cohort. Their details are as shown:')
    for i in stuDict:
        #if (stuDict[i] == nameStu):
        print('\t','Student Name [',i,'], Grades: ', stuDict[i],'\n')

    avgStu = input('Which student do you want to find his/her average? ')
    
    ##############
    recordExist = False
    toAverage = 0
    # if name does not exist, below line for finding length will return error
    # recordExist = len(stuDict[nameStu])

    for i in stuDict:
        if (i == avgStu):
            print('You have entered: ',i,'\n')
            print(i,'records found and grades as shown:',stuDict[i],'\n')
            toAverage = i
            recordExist = True
       
    ##############
    if recordExist == True:
        print('\n','The average records are as shown:','\n')
        # attempts to down to 2 decimal place for average 
        # 
        # hmmm, i use comma, does not work and didn't give me an error 
        # print('\t','Student Name [',toAverage,'], Average Grades:{:.2f} ', format(stat.mean(stuDict[toAverage])),'\n')

        # from Example 1, same format, but switch the arrangement. It did not work and didn't give me an error
        # print('\t','Student Name [',toAverage,'], Average Grades: %.2f','\n' % round(stat.mean(stuDict[toAverage]),2))

        # below are the WORKING ones
        # Example 1
        # print("%.2f" % round(a, 2)) --- does not requires a comma
        print('Below shows different methods of presenting 2 decimal places, see codes')
        print('\t','Student Name [',toAverage,'], Average Grades: %.2f' % round(stat.mean(stuDict[toAverage]),2),'\n')
        # Example 2
        # print("{:.2f}".format(a)) --- does not requires a comma, rather it uses a fullstop 
        print('\t','Student Name [',toAverage,'], Average Grades: {:.2f}'. format(stat.mean(stuDict[toAverage])),'\n')
        # Example 3
        # print("%.2f" % a) --- does not requires a comma 
        print('\t','Student Name [',toAverage,'], Average Grades: %.2f' %(stat.mean(stuDict[toAverage])),'\n')

    else:
        print('You have entered a invalid student name [',avgStu,']')
          
    input('Hit ENTER to go back to MAIN MENU') 


# MAIN MENU
sessionLogin, userID = logInSession()

if sessionLogin == True:
    main(userID)
else:
    print('Goodbye')