# For MSSD Application
# Program by: tkokhing

from msvcrt import getch

def guessWord(wordGuess):
    
    gameSession = 10
    puzzleList = list(wordGuess.upper())
    tempList = []
    tempListIndex = []
    wordLen = len(wordGuess)
    wordGuessUpper = wordGuess.upper()

    # create a tempList based on the length of the word
    # to slowly reveal the puzzle word
    for i in range (0, wordLen):
        tempList.append('?')

    print('\n','Welcome to the guessing game! You got 10 attempts','\n')  

    # find the position(s) of the letter in the word
    while gameSession != 0:
        
        if (gameSession == 3):
            print('\n\n','You have 3 more attempts')
        elif (gameSession == 2):
            print('\n\n','You have 2 more attempts')
        elif (gameSession == 1):
            print('\n\n','Warning!!! This is your last attempt')

       
        inputChar = input('Please enter a Letter: ')

        player1Guess = inputChar.upper()
        # count down for 10 attempts as requied by the question
        gameSession -= 1   

        # test for the letter
        pos = wordGuessUpper.find(player1Guess)
        if pos >= 0:
            # search the entire List to find the letter
            # write its index position to tempListIndex
            for i in range (0, wordLen):
                if puzzleList[i] == player1Guess:
                    tempListIndex.extend([i])
                     
            # insert the guess correctly letter into tempList based 
            # on the position of the letter of the word
            for index in tempListIndex:
                tempList[index] = player1Guess
            
            # clear for next input
            tempListIndex.clear()
           
            if (puzzleList == tempList):
                print('\n\n\n','BINGO, you got it right. Go claim a prize from Alina, yeah!!!','\n\n\n')
                print('=================== Yeah! ==================')
                print('\n',tempList,'\n')
                print('============================================','\n')
                input()
                gameSession = 0
            # display in position as required in the Question
            else:
                print('\n','Hmmm...: ')
                print('======================================')
                print('\n',tempList,'\n')
                print('======================================','\n')
            # mask off the letter or letters that has been revealed with ~
            # normally players will not reenter the same letter silly 
            # but I just want to take care of nuisance 
            wordMask = wordGuessUpper.replace(player1Guess,'~')
            wordGuessUpper = wordMask
        
        else:
            if gameSession == 0:
                print('Too bad, all 10 attempts exhausted!')
            else:
                print('Letter', player1Guess,'not found or already revealed, hit ENTER to continue or ESC to return to Game Master Menu')
                key = getch()
                if key == b'\x1b':
                    gameSession = 0
                else:
                    print('==========  Game on!  ===========','\n')
        
    #return none 
 
def main():
    thissessionLogIn = True
    
    while thissessionLogIn == True:
        print('\n')
        print('===================Hangman Game====================','\n')
        print('===================================================','\n')
        print('\t','Hello Game Master, please choose a word for Player 1 to guess')
        print('\t','[1] - ALPHABET')
        print('\t','[2] - WEDNESDAY')
        print('\t','[3] - OCTOBER')
        print('\t','[4] - DEPARTMENT')
        print('\t','[5] - PROGRAM')
        print('\t','[6] - PLACEMENT')
        print('\t','[0] - Exit','\n')
        sessionInput=input('Which word would you like Player 1 to choose? (Enter a number) ')

        if sessionInput == '1':
            print('You have enter 1')
            guessWord('Alphabet')

        elif sessionInput == '2':
            print('You have enter 2')
            guessWord('Wednesday')
        
        elif sessionInput == '3':
            print('You have enter 3')
            guessWord('October')

        elif sessionInput == '4':
            print('You have enter 4')
            guessWord('Department')

        elif sessionInput == '5':
            print('You have enter 5')
            guessWord('Program')

        elif sessionInput == '6':
            print('You have enter 6')
            guessWord('Placement')


        elif sessionInput == '0':
            print('You have enter 0')
            # sessionLogIn = 1
            thissessionLogIn = False
 
        else:
            print('Please enter a correct option')


main()
print('Thank you SUTD for the opportunity')
input()
