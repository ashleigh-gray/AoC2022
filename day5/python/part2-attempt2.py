import pandas as pd
import re 
import numpy as np

testing = False
columns = 9

class move():
    def __init__(self, input):
        self.input = input
        numbers = re.findall(r'\b\d+\b',input)
        self.number = int(numbers[0])
        self.start = int(numbers[1])-1
        self.end = int(numbers[2])-1
        
class column_height():
    def __init__(self, input):
        self.height = input
        self.hf_height = input+1

if testing == True:
    moves_filename = "../sample_input_moves.txt"
    crates_filename = "../sample_input_crates.txt"
elif testing == False:
    moves_filename = "../input_moves.txt"
    crates_filename = "../input_crates.txt"
    
df = pd.read_csv(crates_filename, names=range(0,columns))
df = df.iloc[::-1]
df = df.reset_index(drop=True)

moves_input = open(moves_filename, 'r')
moves = moves_input.readlines()

move_list = []
heights = {}
for i in range(columns):
    column = df[i]
    for index, row in column.items():
        if pd.notna(row):
            height = index
    heights[i] = column_height(height)

for step in moves:
    current_move = move(step)
    move_list.append(current_move)
    
    start_height = heights[current_move.start].height
    end_height = heights[current_move.end].height
    for m in range(current_move.number):
        df.at[end_height+1+m,current_move.end] = df.at[start_height-(current_move.number-m)+1, current_move.start]
        df.at[start_height-(current_move.number-m)+1, current_move.start] = np.NaN
        heights[current_move.start].height -= 1
        heights[current_move.end].height += 1
            
df = df.dropna(how='all')

final_answer = ''
for j in range(columns):
    if heights[j].height > -1:
        final_answer += df.at[heights[j].height,j][1]
print("-----------------")
print(df.to_string())
print("-----------------")
print("Final answer:", final_answer)

    
    
    
    
    
    


