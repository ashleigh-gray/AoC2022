import string

testing = False

class rucksack_items:
    def __init__(self, input):
        self.input = input
        self.length = len(input)
        self.halflength = int(self.length/2)
        self.half1 = input[0:self.halflength]
        self.half2 = input[self.halflength:self.length]
        self.shared = ''.join(set(self.half1).intersection(self.half2))
        self.priority = priorities[self.shared]      

priorities = dict()
for index, letter in enumerate(string.ascii_letters):
   priorities[letter] = index + 1

if testing == True:
    filename = "../sample_input.txt"
elif testing == False:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.readlines()

rucksacks = []
for line in lines:
    rucksack = rucksack_items(line)
    rucksacks.append(rucksack.priority)
    
print(sum(rucksacks))