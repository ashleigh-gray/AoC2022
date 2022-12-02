# A = rock
# B = paper
# C = scissors

# X = rock
# Y = paper
# Z = scissors

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
        if self.input2 == "X": #You play rock
            self.itemScore = 1
            if self.input1 == "C": #They play scissors
                self.winScore = 6
            elif self.input1 == "A": #They play rock
                self.winScore = 3
            elif self.input1 == "B": #They play paper
                self.winScore = 0
        elif self.input2 == "Y": #You play paper
            self.itemScore = 2
            if self.input1 == "A": #They play rock
                self.winScore = 6
            elif self.input1 == "B": #They play paper
                self.winScore = 3
            elif self.input1 == "C": #They play scissors
                self.winScore = 0
        elif self.input2 == "Z": #You play scissors
            self.itemScore = 3
            if self.input1 == "B": #They play paper
                self.winScore = 6
            elif self.input1 == "C": #They play scissors
                self.winScore = 3
            elif self.input1 == "A": #They play rock
                self.winScore = 0
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
