class Participant:
  def __init__(self, name):
    print('I am here Participant_init start')
    self.name = name
    self.points = 0
    self.choice = ""
    print('I am here Participant_init end')
  def choose(self):
    print('I am here choose start')
    self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
    print("{name} selects {choice}".format(name=self.name, choice = self.choice))
    print('I am here choose end')
  def toNumericalChoice(self):
    print('I am here toNumericalChoice def')
    switcher = {
      "rock": 0,
      "paper": 1,
      "scissor": 2
      }
    return switcher[self.choice]

  def incrementPoint(self):
    print('I am here incrementPoint def')
    self.points += 1

class GameRound:
  def __init__(self, p1, p2):
    print('I am here GameRound start')
    self.rules = [
      [0, -1, 1],
      [1, 0, -1],
      [-1, 1, 0]
    ]
    p1.choose()
    p2.choose()
    result = self.compareChoices(p1,p2)
    print("Round resulted in a {result}".format(result = self.getResultAsString(result)))
    
    if result > 0:
      p1.incrementPoint()
    elif result < 0:
      p2.incrementPoint()
    
    print('I am here GameRound end')

  def compareChoices(self, p1, p2):
    print('I am here ..... compareChoices def')
    return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

  def awardPoints(self):
    print('I am here ..... awardPoints def')
    print("implement")

  def getResultAsString(self, result):
    print('I am here ..... getResultAsString def')
    res = {
      0: "draw",
      1: "win",
      -1: "loss"
    }
    return res[result]

class Game:
  def __init__(self):
    print('I am here Game start')
    self.endGame = False
    self.participant = Participant("Spock")
    self.secondParticipant = Participant("Kirk")
    print('I am here Game end')
  def start(self):
    print('I am here start start')
    # game_round = GameRound(self.participant, self.secondParticipant)
    while not self.endGame:
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()
    print('I am here start end')

  def checkEndCondition(self):
    print('I am here ..... checkEndCondition def')
    answer = input("Continue game y/n")
    if answer == 'y':
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()
    else:
      print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
      self.determineWinner()
      self.endGame = True

  def determineWinner(self):
    print('I am here ..... determineWinner def')
    resultString = "It's a Draw"
    if self.participant.points > self.secondParticipant.points:
      resultString = "Winner is {name}".format(name=self.participant.name)
    elif self.participant.points < self.secondParticipant.points:
      resultString = "Winner is {name}".format(name=self.secondParticipant.name)
    print(resultString)

game = Game()
game.start()


"""
Output of the above testing:
I am here Game start
I am here Participant_init start      
I am here Participant_init end        
I am here Participant_init start      
I am here Participant_init end        
I am here Game end
I am here start start
I am here GameRound start
I am here choose start
Spock, select rock, paper or scissor: paper
Spock selects paper
I am here choose end
I am here choose start
Kirk, select rock, paper or scissor: paper
Kirk selects paper     
I am here choose end   
I am here GameRound end
I am here start end    
"""




"""
This is the result after beautifying the codes following the instructions, 

I am here Game start
I am here Participant_init start      
I am here Participant_init end        
I am here Participant_init start      
I am here Participant_init end        
I am here Game end
I am here start start
I am here GameRound start
I am here choose start
Spock, select rock, paper or scissor: paper
Spock selects paper
I am here choose end
I am here choose start
Kirk, select rock, paper or scissor: paper
Kirk selects paper
I am here choose end

##### below were added
I am here ..... compareChoices def   
I am here toNumericalChoice def      
I am here toNumericalChoice def      
I am here ..... getResultAsString def
Round resulted in a draw
##### above were added

I am here GameRound end

##### below were added
I am here ..... checkEndCondition def
Continue game y/nn
Game ended, Spock has 0, and Kirk has 0
I am here ..... determineWinner def    
It's a Draw
##### above were added

I am here start end



"""
