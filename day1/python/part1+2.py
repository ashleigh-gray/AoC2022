input = open('../input.txt', 'r')
lines = input.readlines()

elf_count = 0
elves = {}
calories = 0
for line in lines:
    if line == '\n':
        elves[elf_count] = calories
        calories = 0
        elf_count += 1
    else:
        calories = calories + int(line)
      
sorted_elves = {k: v for k,v in sorted(elves.items(), key = lambda item: item[1], reverse=True)}

print("Top calories:", list(sorted_elves.values())[0])
print("Top 3 calories:", list(sorted_elves.values())[0]+list(sorted_elves.values())[1]+list(sorted_elves.values())[2])