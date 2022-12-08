import pandas as pd
import numpy as np

testing = False

class tree:
    def __init__(self,input,x,y):
        self.height = int(input)
        self.coords = (x,y)
        self.top = 0
        self.left = 0
        self.right = 0
        self.bottom = 0
    
    def get_score(self):
        return self.top * self.bottom * self.right * self.left

        
if testing == True:
    filename = "../sample_input.txt"
    n = 5
elif testing == False:
    filename = "../input.txt"
    n = 99
    
df = pd.read_csv(filename, names=["temp"], dtype={'temp': str})
df = pd.DataFrame(np.stack(df.temp.apply(list).values))
df = df.astype('int32')

trees = []

for x in range (0,n):
    for y in range (0,n):
        current = tree(df.at[x,y],x,y)
        trees.append(current)
        if x > 0: # only check the top if there's something above
            for i in range(x,-1,-1)[1:]:
                current.top += 1
                if df.at[i,y] >= df.at[x,y]:
                    break
        if x < n:
            for j in range(x,n)[1:]:
                current.bottom += 1
                if df.at[j,y] >= df.at[x,y]:
                    break
        if y > 0:
            for a in range(y,-1,-1)[1:]:
                current.left += 1
                if df.at[x,a] >= df.at[x,y]:
                    break
        if y < n:
            for b in range(y,n)[1:]:
                current.right += 1
                if df.at[x,b] >= df.at[x,y]:
                    break
        
scores = []
for t in trees:
    scores.append(t.get_score())

print("Top score:", max(scores))