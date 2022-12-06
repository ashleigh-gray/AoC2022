testing = 0

if testing == 1:
    filename = "../sample_input_1.txt"
elif testing == 2:
    filename = "../sample_input_2.txt"
elif testing == 3:
    filename = "../sample_input_3.txt"
elif testing == 4:
    filename = "../sample_input_4.txt"
elif testing == 5:
    filename = "../sample_input_5.txt"
elif testing == 0:
    filename = "../input.txt"
    
input = open(filename, 'r')
signal = input.readlines()[0]

start = signal[0:3]
remainder = signal[3:]

char_no = 4
for i in remainder:
    test = start + i
    if len(set(test)) == 4:
        print("found 4 unique at position", char_no)
        break
    else:
        start = test[1:]
    char_no += 1
    