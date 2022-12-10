import pandas as pd
import numpy as np

testing = True

class square():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.visited = False
        

if testing == True:
    filename = "../sample_input.txt"
elif testing == False:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.read().splitlines()

# Get max size of grid

A = 1
B = 1

for line in lines:
    direction = line.split(' ')[0]
    number = int(line.split(' ')[1])
    if direction in ['R', 'L']:
        if number > B:
            B = number
    elif direction in ['U', 'D']:
        if number > A:
            A = number
            
A += 1
B += 1
            
# Grid is AxB wide

visited = []

df = pd.DataFrame(columns=range(B), index=range(A))

df.at[A-1,0] = "H"

H_current_x = A-1
H_current_y = 0

T_current_x = A-1
T_current_y = 0
previous_dir = ''

for line in lines:
    direction = line.split(' ')[0]
    number = int(line.split(' ')[1])
    print("-----------------------------")
    print(df.to_string())
    print("Head current X:", H_current_x)
    print("Head current Y:", H_current_y)
    print("Tail current X:", T_current_x)
    print("Tail current Y:", T_current_y)
    print("Previous direction:", previous_dir)
    print("Current direction:", direction)
    df.at[H_current_x, H_current_y] = np.NAN
    df.at[T_current_x, T_current_y] = np.NAN
    if direction == 'U':
        print("moving up, tail at:", T_current_x, T_current_y) 
        df.at[H_current_x-number,H_current_y] = "H"
        if previous_dir in ['R', 'L']:
            print("turning corner")
            if H_current_y < T_current_y:
                visited.append([(i,T_current_y-1) for i in range(T_current_x-number,T_current_x)[1:]])
                df.at[T_current_x-number+1,H_current_y-1] = "T"
                T_current_y -= 1
            else:
                visited.append([(i,T_current_y+1) for i in range(T_current_x-number,T_current_x)[1:]])
                df.at[T_current_x-number+1,H_current_y+1] = "T"
                T_current_y += 1
            
            H_current_x = H_current_x-number
            T_current_x = T_current_x-number+1
            
        else:
            df.at[T_current_x-number+1,T_current_y] = "T"
            visited.append([(i,T_current_y) for i in range(T_current_x,T_current_x-number)])
            H_current_x = H_current_x-number
            T_current_x = T_current_x-number+1

    elif direction == 'D':
        print("moving down, tail at:", T_current_x, T_current_y) 
        df.at[H_current_x+number,H_current_y] = "H"
        if previous_dir in ['R', 'L']:
            print("turning corner")
            if H_current_y > T_current_y:
                visited.append([(i,T_current_y-1) for i in range(T_current_x,T_current_x+number)[1:]])
                df.at[T_current_x+number+1,H_current_y-1] = "T"
                T_current_y -= 1
            else:
                visited.append([(i,T_current_y+1) for i in range(T_current_x,T_current_x+number)[1:]])
                df.at[T_current_x+number+1,H_current_y+1] = "T"
                T_current_y += 1
            
            H_current_x = H_current_x+number
            T_current_x = T_current_x+number+1
            
        else:   
            df.at[T_current_x+number+1,T_current_y] = "T"
            visited.append([(i,T_current_y) for i in range(T_current_x,T_current_x+number)])
            H_current_x = H_current_x+number
            T_current_x = T_current_x+number+1
        
    elif direction == 'L':
        print("moving left, tail at:", T_current_x, T_current_y) 
        df.at[H_current_x,H_current_y-number] = "H"
        if previous_dir in ['U', 'D']:
            print("turning corner")
            if H_current_x < T_current_x:
                visited.append([(T_current_x-1,i) for i in range(T_current_y-number,T_current_y)[1:]])
                df.at[T_current_x-1,H_current_y-number+1] = "T"
                T_current_x -= 1
            else:
                visited.append([(T_current_x+1,i) for i in range(T_current_y-number,T_current_y)[1:]])
                df.at[T_current_x+1,H_current_y-number+1] = "T"
                T_current_x += 1
            H_current_y = H_current_y-number
            T_current_y = T_current_y-number+1
        else:
            df.at[T_current_x,T_current_y-number+1] = "T"
            visited.append([(T_current_x,i) for i in range(T_current_y,T_current_y-number)])
            H_current_y = H_current_y-number
            T_current_y = T_current_y-number+1
        
    elif direction == 'R':
        print("moving right, tail at:", T_current_x, T_current_y)       
        df.at[H_current_x,H_current_y+number] = "H"
        if previous_dir in ['U', 'D']:
            print("turning corner") 
            if H_current_x < T_current_x:
                visited.append([(T_current_x-1,i) for i in range(T_current_y,T_current_y+number)[1:]])
                df.at[H_current_x-1,T_current_y+number-1] = "T"
                T_current_x -= 1
            else:
                visited.append([(T_current_x+1,i) for i in range(T_current_y,T_current_y+number)[1:]])
                df.at[H_current_x+1,T_current_y+number-1] = "T"
                T_current_x += 1
            H_current_y = H_current_y+number
            T_current_y = T_current_y+number-1
            
        else:
            df.at[T_current_x,T_current_y+number-1] = "T"
            visited.append([(T_current_x,i) for i in range(T_current_y,T_current_y+number)])
            H_current_y = H_current_y+number
            T_current_y = T_current_y+number-1
    print("Tail moved to:", T_current_x, T_current_y)
    print("Head moved to:", H_current_x, H_current_y)
    previous_dir = direction

print(df.to_string())

final = list(set([item for sublist in visited for item in sublist])) 
print(final)  
print(len(final))
print(visited)

# [[(4, 0), (4, 1), (4, 2), (4, 3)], [(1, 4), (2, 4), (3, 4)], [(0, 2), (0, 3)], []]
# [[(4, 0), (4, 1), (4, 2), (4, 3)], [(1, 4), (2, 4), (3, 4)], [(0, 2), (0, 3)], [], [(3, 2), (3, 3), (3, 4)]]


# [(2, 4), (4, 0), (3, 4), (4, 3), (3, 1), (0, 3), (1, 4), (4, 2), (2, 3), (0, 2), (3, 3), (2, 2), (3, 2), (4, 1)]

# [(4,0),(4,1),(4,2),(4,3),(3,4),(2,4),(1,4),(0,3),(0,2),(1,3),(2,1),(2,2),(2,3)]


# [[(4, 0), (4, 1), (4, 2), (4, 3)], 
#  [(1, 4), (2, 4), (3, 4)], 
#  [(0, 2), (0, 3)], 
#  [], 
#  [(2, 2), (2, 3), (2, 4)], 
#  [], 
#  [(3, 1), (3, 2), (3, 3), (3, 4)], 
#  [(4, 1), (4, 2)]]