import pandas as pd
import numpy as np

testing = False

class tree:
    def __init__(self,input,x,y):
        # True means visible
        # False means hidden
        self.height = int(input)
        self.coords = (x,y)
        self.top = True
        self.left = True
        self.right = True
        self.bottom = True
    
    def is_hidden(self):
        if self.top == self.bottom == self.right == self.left == False:
            return True
        else:
            return False
        
if testing == True:
    filename = "../sample_input.txt"
    real_n = 5
    n = real_n -1
elif testing == False:
    filename = "../input.txt"
    real_n = 99
    n = real_n - 1
    
df = pd.read_csv(filename, names=["temp"], dtype={'temp': str})
df = pd.DataFrame(np.stack(df.temp.apply(list).values))
df = df.astype('int32')

trees = []
visible = 4*n

for x in range (1,n):
    for y in range (1,n):
        current = tree(df.at[x,y],x,y)
        trees.append(current)
        for i in range(0,x):
            if df.at[i,y] >= df.at[x,y]:
                current.top = False
                break
        for j in range(x,n+1)[1:]:
            if df.at[j,y] >= df.at[x,y]:
                current.bottom = False
                break
        for a in range(0,y):
            if df.at[x,a] >= df.at[x,y]:
                current.left = False
                break
        for b in range(y,n+1)[1:]:
            if df.at[x,b] >= df.at[x,y]:
                current.right = False
                break
        if current.is_hidden() == False:
            visible += 1
            
print("Number of visible trees:", visible)