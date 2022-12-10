import numpy as np

testing = False

move_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

class knot:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.tail_visits = {tuple([0, 0])}
    
    def move_head(self, direction):
        move = move_dict[direction]
        self.head = np.add(self.head,move).tolist()
        diff = np.subtract(self.head,self.tail).tolist()
        self.move_tail(diff)
        
    def move_tail(self,diff):
        # Only moved within the 1 tile radius of the head, tail doesn't move
        if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
            return
        elif abs(diff[0]) == 2 and abs(diff[1]) == 2:
            self.tail = [self.tail[0] + np.sign(diff[0]), self.tail[1] + np.sign(diff[1])]
        elif abs(diff[0]) == 2:
            self.tail = [self.tail[0] + np.sign(diff[0]), self.head[1]]
        elif abs(diff[1]) == 2:
            self.tail = [self.head[0],self.tail[1] + np.sign(diff[1])]
        self.tail_visits.add(tuple(self.tail))

if testing == True:
    filename = "../sample_input.txt"
elif testing == False:
    filename = "../input.txt"
    
input = open(filename, 'r')
lines = input.read().splitlines()

rope = knot()
for line in lines:
    direction = line.split(' ')[0]
    number = int(line.split(' ')[1])
    for i in range(number):
        rope.move_head(direction)
# print(rope.tail_visits)
print(len(rope.tail_visits))
    # total_move = knot.get_move(direction,number)
    # rope.move_head(total_move)
    # print(rope.head, rope.tail)
    
