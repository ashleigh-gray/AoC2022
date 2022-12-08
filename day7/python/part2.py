testing = False

class file:
    def __init__(self, input, pwd):
        split = input.split(' ')
        self.size = int(split[0])
        self.filename = split[1]
        file_pieces = self.filename.split('.')
        self.name = file_pieces[0]
        if len(file_pieces) == 1:
            file_pieces.append('')
        self.extension = file_pieces[1]
        self.wd = pwd
        
class folder:
    def __init__(self, input, pwd):
        self.name = input.split(' ')[1]
        self.files = []
        self.size = 0
        full_path = ''
        for x in pwd:
            full_path = full_path + x
        self.fullpath = full_path + self.name
        
    def add_file_to_folder(self, input):
        self.files.append(input)
        self.size += int(input.size)
        
    def add_folder_to_folder(self, input):
        self.size += int(input.size)

if testing == True:
    filename = "../sample_input.txt"
elif testing == False:
    filename = "../input.txt"
    
    
dirs = [folder("dir /", "")]
files = []
input = open(filename, 'r')
lines = input.read().splitlines()
pwd = []

for line in lines:
    if line[0:4] == "$ ls":
        continue
    elif line[0:4] == "$ cd":
        command = line.split(' ')
        if command[2] == "..":
            pwd.pop()
        else:
            if command[2] == "/":
                pwd.append("/")
            else:
                pwd.append(command[2])
    elif line[0:3] == "dir":
        dirs.append(folder(line, pwd))
    else:
        for i in dirs:
            if i.fullpath in ''.join(pwd):
                folder.add_file_to_folder(i, file(line, pwd))
                
total_sum = 0
outer_size = 0
disk_size = 70000000
needed_size = 30000000
outer_size = dirs[0].size
left_to_free = needed_size-(disk_size-outer_size)
candidates = []

for d in dirs:
    if d.size >= left_to_free:
        candidates.append((d.fullpath, d.size))

sorted = sorted(candidates, key=lambda value: value[1])
print(sorted[0])
                
