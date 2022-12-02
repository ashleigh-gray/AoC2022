# A = rock
# B = paper
# C = scissors

# X = lose
# Y = draw
# Z = win

# 1 point for rock
# 2 points for paper
# 3 points for scissors 

# 0 points for loss
# 3 points for draw
# 6 points for win 

class roundScore:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.itemScore = 0
        self.winScore = 0
        
    def getScore(self):
        if self.input2 == "X": #You must lose
            self.winScore = 0
            if self.input1 == "C": #They play scissors - you play paper
                self.itemScore= 2
            elif self.input1 == "A": #They play rock - you play scissors
                self.itemScore = 3
            elif self.input1 == "B": #They play paper - you play rock
                self.itemScore = 1
        elif self.input2 == "Y": #You must draw
            self.winScore = 3
            if self.input1 == "A": #They play rock - you play rock
                self.itemScore = 1
            elif self.input1 == "B": #They play paper - you play paper
                self.itemScore = 2
            elif self.input1 == "C": #They play scissors - you play scissors
                self.itemScore = 3
        elif self.input2 == "Z": #You must win
            self.winScore = 6
            if self.input1 == "B": #They play paper - you play scissors
                self.itemScore = 3
            elif self.input1 == "C": #They play scissors - you play rock
                self.itemScore = 1
            elif self.input1 == "A": #They play rock - you play paper
                self.itemScore = 2
        self.totalScore = self.itemScore + self.winScore
        return self.totalScore
        

input = open('../input.txt', 'r')
lines = input.readlines()

rounds = []
for line in lines:
    inputs = line.split()
    score = roundScore(inputs[0],inputs[1])
    rounds.append(score.getScore())
    
print("Total score:", sum(rounds))
