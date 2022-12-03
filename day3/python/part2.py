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

badges = []
total_elves = len(lines)
groups = int(total_elves/3)

i = 0
for group in range(groups):
    elf_1 = rucksack_items(lines[i].strip('\n'))
    elf_2 = rucksack_items(lines[i+1].strip('\n'))
    elf_3 = rucksack_items(lines[i+2].strip('\n'))
    trio = ''.join(set(elf_1.input).intersection(elf_2.input).intersection(elf_3.input))
    badges.append(priorities[trio])
    i += 3
    
print(sum(badges))