testing = 0
    
def get_sprite_neighbours(x):
    return [x-1, x, x+1]

def sprite_in_pixel(pixel, x):
    if pixel in get_sprite_neighbours(x):
        return True
    else:
        return False
    
def draw_pixel(pixel, row):
    return row[:pixel] + on + row[pixel + 1:]

def print_rows(rows):
    print(row[0:40])
    print(row[40:80])
    print(row[80:120])
    print(row[120:160])
    print(row[160:200])
    print(row[200:240])

if testing == 1:
    filename = "../sample_input1.txt"
elif testing == 2:
    filename = "../sample_input2.txt"
elif testing == 0:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.read().splitlines()

addxs = [ line for line in lines if 'addx' in line]
noops = [ line for line in lines if 'noop' in line]

cycles = len(noops) + 2*len(addxs)

signals = []
off = " "
on = u"\u2588"

row = off*cycles

instructions = {}

cycle_no = 1
x = 1 

for line in lines:
    if 'noop' in line:
        instructions[cycle_no] = get_sprite_neighbours(x)
        cycle_no += 1
        continue
    elif 'addx' in line:
        change = int(line.split(' ')[1])
        instructions[cycle_no] = get_sprite_neighbours(x)
        cycle_no += 1
        x = x + change
        instructions[cycle_no] = get_sprite_neighbours(x)
        cycle_no += 1
        
for i in instructions:
    if i%40 == 0:
        if 0 in instructions[i]:
            row = draw_pixel(i, row)
    else:
        if i%40 in instructions[i]:
            row = draw_pixel(i, row)
        
print_rows(row)
