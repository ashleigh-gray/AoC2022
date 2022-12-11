testing = 2

def get_signal_strength(cycle_no, register):
    return cycle_no * register

def is_break_cycle(cycle_no):
    if cycle_no in break_cycles:
        return True
    else:
        return False

if testing == 1:
    filename = "../sample_input1.txt"
elif testing == 2:
    filename = "../sample_input2.txt"
elif testing == 0:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.read().splitlines()

break_cycles = [20, 60, 100, 140, 180, 220]
signals = []

cycle_no = 1
x = 1
for line in lines:
    if 'noop' in line:
        if is_break_cycle(cycle_no):
            signals.append((cycle_no, get_signal_strength(cycle_no,x)))
        cycle_no += 1
        continue
    elif 'addx' in line:
        change = int(line.split(' ')[1])
        if is_break_cycle(cycle_no):
            signals.append((cycle_no, get_signal_strength(cycle_no,x)))
        cycle_no += 1
        if is_break_cycle(cycle_no):
            signals.append((cycle_no, get_signal_strength(cycle_no,x)))
        x = x + change
        cycle_no += 1
        
print("All signal strengths:", signals)
print("Sum:", sum([y for _,y in signals]))