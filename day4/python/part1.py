testing = False

class elf_sections:
    def __init__(self, input):
        self.input = input
        
    def expand_range(self):
        done = False
        current = int(self.input.split('-')[0])
        range = []
        end = int(self.input.split('-')[1])
        while done == False:
            range.append(current)
            current =+ current + 1 
            if current > end:
                done = True
        self.range = range

if testing == True:
    filename = "../sample_input.txt"
elif testing == False:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.readlines()

total_overlap = []

for line in lines:
    elf1 = elf_sections(line.split(',')[0])
    elf2 = elf_sections(line.split(',')[1])
    elf1.expand_range()
    elf2.expand_range()
    if set(elf1.range).issubset(set(elf2.range)):
        total_overlap.append(line.strip('\n'))
    elif set(elf2.range).issubset(set(elf1.range)):
        total_overlap.append(line.strip('\n'))
        
print("total overlap:", len(total_overlap))
